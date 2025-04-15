import json
import requests

class CustomConnector():
    def __init__(self, config: dict):
        self.url = config.get("url")
        self.api_key = config.get("api_key")
        self.verify_ssl = config.get("verify_ssl")
        self.headers = {
            "Appkey": self.api_key,
            "Content-Type": "application/json",
            "accept": "application/json;odata.metadata=minimal;odata.streaming=true",
        }

    def check_health(self, config: dict, params: dict=None) -> dict:
        try:
            r_url = self.url + "/api/external/v1/connectors/cards"
            
            resp = requests.request("GET", r_url, headers=self.headers, verify=self.verify_ssl)
            if resp.status_code == 200:
                return resp.json()
            raise Exception(f"{resp.content}")
        except Exception as err:
            raise Exception(str(err))

    def generic_api_call(self, config: dict, params: dict) -> dict:
        try:
            r_url = self.url + params.get("api_endpoint")

            p_method = params.get("method")
            p_data = json.dumps(params.get("data")) if isinstance(params.get("data"), dict) else None
            p_params = params.get("params") if isinstance(params.get("params"), dict) else None
            
            resp = requests.request(p_method, r_url, headers=self.headers, data=p_data, params=p_params, verify=self.verify_ssl)
            if resp.status_code == 200:
                return resp.json()
            raise Exception(f"{resp.content}")
        except Exception as err:
            raise Exception(str(err))