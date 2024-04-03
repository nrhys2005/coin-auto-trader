import hashlib
import uuid
from urllib.parse import unquote, urlencode

import httpx
import jwt

from config.config import SECRET_KEY, ACCESS_KEY
from config.upbit_config import base_url, accounts_api_url


class Upbit:
    def __init__(self):
        self.secret_key = SECRET_KEY
        self.access_key = ACCESS_KEY

    @property
    def headers(self) -> dict:
        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
        }
        # if query_hash:
        #     payload['query_hash'] = query_hash
        #     payload['query_hash_alg'] = 'SHA512'

        jwt_token = jwt.encode(payload, SECRET_KEY)
        headers = {"Authorization": f"Bearer {jwt_token}"}
        return headers

    def get_payload(self, **params) -> dict:
        query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

        m = hashlib.sha512()
        m.update(query_string)
        query_hash = m.hexdigest()

        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }
        return payload

    async def get_accounts(self) -> list[dict]:
        async with httpx.AsyncClient() as client:
            url = base_url+accounts_api_url
            headers = self.headers
            try:
                response = await client.get(url, headers=headers)
                if response.status_code == 200:
                    data = response.json()
                    return data
                else:
                    return []
            except httpx.RequestError as e:
                # 요청 에러 처리
                print(f"Request error: {e}")
                return []
            except httpx.HTTPStatusError as e:
                # 응답 에러 처리
                print(f"HTTP status error: {e}")
                return []

    async def post_orders(self) -> list[dict]:
        async with httpx.AsyncClient() as client:
            url = base_url+accounts_api_url
            headers = self.headers
            try:
                response = await client.get(url, headers=headers)
                if response.status_code == 200:
                    data = response.json()
                    return data
                else:
                    return []
            except httpx.RequestError as e:
                # 요청 에러 처리
                print(f"Request error: {e}")
                return []
            except httpx.HTTPStatusError as e:
                # 응답 에러 처리
                print(f"HTTP status error: {e}")
                return []
