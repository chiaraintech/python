import requests

def get_data() -> dict:
    request = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    data: dict = request.json()

    return data

    # happy path: good link with json returned
    # when we create a test however that data can change
    # MUST create a standard response back