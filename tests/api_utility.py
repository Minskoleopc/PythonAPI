import requests

class APIUtility:
    """Utility class to handle API requests"""

    def __init__(self, base_url):
        self.base_url = base_url

    def send_request(self, method, endpoint, params=None, json=None):
        """Generic method to send API requests"""
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, params=params, json=json)
        return self._handle_response(response)

    def get(self, endpoint, params=None):
        """Handles GET requests"""
        return self.send_request("GET", endpoint, params=params)

    def post(self, endpoint, json):
        """Handles POST requests"""
        return self.send_request("POST", endpoint, json=json)

    def put(self, endpoint, json):
        """Handles PUT requests"""
        return self.send_request("PUT", endpoint, json=json)

    def delete(self, endpoint):
        """Handles DELETE requests"""
        return self.send_request("DELETE", endpoint)

    def _handle_response(self, response):
        """Handles API responses, checks for errors"""
        try:
            response.raise_for_status()
            return {
                "status_code": response.status_code,  # Ensure status_code is returned
                "data": response.json() if response.content else None
            }
        except requests.exceptions.HTTPError as err:
            return {"error": str(err), "status_code": response.status_code}
