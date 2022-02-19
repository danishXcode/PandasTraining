from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class



# Press the green button in the gutter to run the script.
def login() -> str:
    try:
        # Create auth token (sign in)
        api_instance = swagger_client.AuthApi()
        body = swagger_client.LoginRequest(login="danish77shaikh2@gmail.com", password="Messi2@10", twofa_code="180768",
                                           remember=True)  # LoginRequest |  (optional)
        api_response = api_instance.auth_login_post(body=body)
        pprint(api_response)
        return api_response.access_token

    except ApiException as e:
        print("Exception when calling AuthApi->auth_login_post: %s\n" % e)


if __name__ == '__main__':
    configuration = swagger_client.Configuration()
    configuration.api_key['Authorization'] = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9hcGkiLCJpYXQiOjE2NDUyNTM2MTUsImV4cCI6MTk2MDYxMzYxNSwibmJmIjoxNjQ1MjUzNjE1LCJqdGkiOjU4NjcyNzA3LCJzdWIiOjU4NjcyNzA3fQ.zdaalFXFbqNNv6hMf9hLT_V8WDwAuKjWqzpP6X-fu24"
    configuration.api_key_prefix['Authorization'] = 'Bearer'
    #api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

    farm_api_isntance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))

    try:
        # Get full account info
       # api_response = api_instance.account_get()
        api_response = farm_api_isntance.farms_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->account_get: %s\n" % e)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
