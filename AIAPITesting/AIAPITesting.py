import requests
from utils import is_api_endpoint

def test_get_api(url):


    #GET request to the API endpoint
    response = requests.get(url)
    
    #Response status code is 200 or failed
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    
    #JSON parsing
    try:
        data = response.json()
        print("Response JSON:", data)
    except ValueError:
        assert False, "Response is not in JSON format"

    #Data assertions
    if "expected_key" in data:
        print("Expected key found in the response.")
    else:
        print("Expected key not found in the response.")

def main():
    #print("API Testing Application. Type 'exit' to quit.")
    
    while True:
        test_url = input("===========================================")
        
        confirm = is_api_endpoint(test_url)

        if test_url.lower() == "exit" or "adios" or "see you" or "close":
            #print("Shutting down")
            break
        
        #Call the test_get_api function with the input URL
        try:
            test_get_api(test_url)
        except AssertionError as e:
            print(f"Test failed: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
