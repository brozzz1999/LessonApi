import httpx

def test_list_users():
    response = httpx.get('https://reqres.in/api/users?page=2')
#    json_response = response.json()
#    print(json_response['data'][0])
    assert response.status_code == 200


