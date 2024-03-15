import json
import posixpath
from copy import deepcopy
from enum import Enum
from http import HTTPStatus
from typing import Coroutine
from urllib.parse import urljoin

from aiohttp import ClientSession

from notion.schemas.paginatable_response import PaginatableResponseSchema
from notion.items.text_blocks import Paragraph

from .response_exceptions import (BadRequest, NotFoundError, NotionIsIll,
                                  Restricted, Unauthorized)

HEADERS_PATTERN = {
    'Authorization': 'Bearer {}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28',
}


# Endpoint data:

BASE_URL = 'https://api.notion.com/v1'


def endpoint(end: str) -> str:
    return urljoin(BASE_URL,
                   posixpath.join(BASE_URL, end))


class Endpoints(str, Enum):
    """https://developers.notion.com/reference/intro#supported-endpoints"""

    children = endpoint('blocks/{block_id}/children')

    all_users = endpoint('users')
    block = endpoint('blocks/{block_id}')
    comments = endpoint('comments')
    databases = endpoint('databases/{}')
    pages = endpoint('pages/{}')
    page_properties = endpoint('pages/{page_id}/properties/{property_id}')


# Classes:

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

    # Service methods:

    def _check_session(self) -> None:
        """Checks session state"""

        if self._session.closed:
            raise EOFError('Session is closed')

    def _process_response(self, response: dict):
        status = response.get('status', None)
        if status:
            if status == HTTPStatus.UNAUTHORIZED:
                raise Unauthorized()
            if status == HTTPStatus.FORBIDDEN:
                raise Restricted()
            if status == HTTPStatus.NOT_FOUND:
                raise NotFoundError()
            repr = f'{status}: {response["code"]}'
            match (status // 100):
                case 4:
                    raise BadRequest(repr)
                case 5:
                    raise NotionIsIll(repr)

    async def _send_request(self, endpoint: str, method: Coroutine,
                            params: dict = None, data: dict = None) -> dict:
        """Sends request to Notion API and returns JSON dict from response"""

        self._check_session()
        params = dict() if params is None else params
        data = dict() if data is None else data

        response = await method(endpoint, headers=self._headers,
                                params=params, data=json.dumps(data))
        response = await response.json()
        # print(response)
        self._process_response(response)
        return response

    # API methods:

    # async def get_block(self, id: str) -> dict:
    #     response = await self._send_request(
    #         endpoint=Endpoints.block.format(block_id=id),
    #         method=self._session.get
    #     )
    #     block_type = response['type']
    #     return response

    async def get_children_of(self, parent: str) -> list[dict]:
        children = list()

        has_more = True
        start_cursor = None
        while has_more:
            response = await self._send_request(
                endpoint=Endpoints.children.format(block_id=parent),
                method=self._session.get,
                params={'start_cursor': start_cursor} if start_cursor else None
            )
            response = PaginatableResponseSchema.model_validate(response)

            children.extend(response.results)
            start_cursor = response.next_cursor
            has_more = response.has_more
        return children
        # return [Paragraph.from_json_dict(child) for child in children]

    async def append_children_to(self, parent: str, children: list) -> None:
        return await self._send_request(
            endpoint=Endpoints.children.format(block_id=parent),
            method=self._session.patch,
            data={'children': [child.dump_json_dict() for child in children]}
        )
