import requests

# Configuration
URL = 'http://google.com'
TIMEOUT = 5  

def check_application_status(url):
    """Check the status of the application."""
    try:
        response = requests.get(url, timeout=TIMEOUT)
        status_code = response.status_code

        if 200 <= status_code < 300:
            return 'UP', status_code
        elif 400 <= status_code < 500:
            return 'DOWN', status_code
        elif 500 <= status_code < 600:
            return 'DOWN', status_code
        else:
            return 'UNKNOWN STATUS', status_code

    except requests.exceptions.Timeout:
        return 'DOWN', None
    except requests.exceptions.RequestException as e:
        return 'DOWN', str(e)

if __name__ == "__main__":
    status, code = check_application_status(URL)
    if code is not None:
        print(f"Application Status: {status} (HTTP Status Code: {code})")
    else:
        print(f"Application Status: {status}")
