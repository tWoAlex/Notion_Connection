import posixpath
import json
from copy import deepcopy
from enum import Enum
from urllib.parse import urljoin
from http import HTTPStatus

from aiohttp import ClientSession

from notion.blocks.base import NotionBlock, BaseBlockRetrieveSchema
from notion.blocks import text

BASE_URL = 'https://api.notion.com/v1'


def endpoint(end: str):
    return urljoin(BASE_URL,
                   posixpath.join(BASE_URL, end))


class Endpoints(str, Enum):
    blocks = endpoint('blocks/{}')
    databases = endpoint('databases/{}')
    pages = endpoint('pages/{}')
    children = endpoint('blocks/{}/children')


HEADERS_PATTERN = {
    'Authorization': 'Bearer {}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28',
}


class NotionConnection:
    def __init__(self, secret_token: str) -> None:
        self._token = secret_token
        self._headers = deepcopy(HEADERS_PATTERN)
        self._headers['Authorization'] = (self._headers['Authorization']
                                          .format(secret_token))

    # As async Context Manager:

    async def __aenter__(self):
        self._session = ClientSession()
        return self

    async def __aexit__(self, exc_type, exc, traceback):
        await self._session.close()

    def _check_session(self):
        if self._session.closed:
            raise EOFError('Session is closed')

    async def _get_block(self, id: str) -> dict | None:
        """Returns JSON[dict of items] response with block info"""
        response = await self._session.get(Endpoints.blocks.format(id),
                                           headers=self._headers)
        if response.status == HTTPStatus.OK:
            return await response.json()

    async def _update_block(self, block: NotionBlock) -> dict | None:
        """Returns JSON[dict of items] response with block info"""
        response = await self._session.patch(Endpoints.blocks.format(block.id),
                                             headers=self._headers,
                                             data=json.dumps(
                                                 block.create_request_json()))
        if response.status == HTTPStatus.OK:
            return await response.json()

    async def _get_page(self, id: str) -> dict | None:
        response = await self._session.get(Endpoints.pages.format(id),
                                           headers=self._headers)
        if response.status == HTTPStatus.OK:
            return await response.json()

    def validate(self, json: str, cls) -> BaseBlockRetrieveSchema:
        return cls.model_validate_json(json)

    async def get_item(self, id: str) -> NotionBlock:
        self._check_session()
        response = await self._get_block(id)
        for block_type in text.block_types:
            if block_type._schematic_type == response['type']:
                return block_type.from_json_dict(response)
        raise ValueError('Block type in response not recognized')

    async def update_item(self, item) -> dict | None:
        self._check_session()
        return await self._update_block(item)

    async def get_children_of(self, parent: str | NotionBlock) -> dict | None:
        if not isinstance(parent, str):
            parent = parent.id

        self._check_session()
        response = await self._session.get(Endpoints.children.format(parent),
                                           headers=self._headers)
        return await response.json()

    async def append_children_to(self,
                                 parent: str | NotionBlock,
                                 children: list[NotionBlock]) -> dict:
        if not isinstance(parent, str):
            parent = parent.id
        children = [child.create_request_json() for child in children]

        self._check_session()
        data = {'children': children}
        response = await self._session.patch(Endpoints.children.format(parent),
                                             headers=self._headers,
                                             data=json.dumps(data))
        return await response.json()
