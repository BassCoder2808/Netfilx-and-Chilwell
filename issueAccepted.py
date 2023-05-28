import sys
import requests

def get_issue_contents(issue_id, access_token):
    base_url = "https://api.github.com"
    owner = "spdx"
    repo = "license-list-XML"

    # API endpoint for retrieving an issue
    endpoint = f"{base_url}/repos/{owner}/{repo}/issues/{issue_id}"

    # Add authentication if required (e.g., access token)
    headers = {
        "Authorization": access_token
    }

    # Send a GET request to retrieve the issue details
    response = requests.get(endpoint, headers=headers)
    
    if response.status_code == 200:
        issue_data = response.json()
        issue_title = issue_data['title']
        issue_body = issue_data['body']
        
        # Process the issue contents as needed
        print("Issue Title:", issue_title)
        print("Issue Body:", issue_body)
    else:
        print("Error occurred while retrieving the issue:", response.status_code, response.text)

# Call the function with the desired issue ID
issue_id = 123
get_issue_contents(issue_id)


if __name__ == "__main__":
    print("Hello from the outer side")
    # if we get here, all passed
    print(f"All licenses and exceptions validated against schema.")
    # Access command-line parameters
    # The first parameter (sys.argv[0]) is the script name itself
    # The subsequent parameters (sys.argv[1:], starting from index 1) are the command-line arguments
    arguments = sys.argv[1:]
    # Process command-line parameters
    arg1 = arguments[0]
    arg2 = arguments[1]
    get_issue_contents(arg1, arg2)