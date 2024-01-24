import requests

def fetch_posts():
    # JSONPlaceholder API endpoint for posts
    api_url = 'https://jsonplaceholder.typicode.com/users/2'

    try:
        # Make a GET request to fetch posts
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            users = response.json()
            print(f"User ID: {users['id']}")
            print(f"User Name: {users['name']}")
            # Display the fetched posts
            #for user in users:
                #print(f"User ID: {user['id']}")
                #print(f"Name: {user['name']}")
                
        else:
            # Display an error message for unsuccessful requests
            print(f"Error: Unable to fetch posts. Status Code: {response.status_code}")
    except requests.RequestException as e:
        # Display an error message for general request exceptions
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_posts()
