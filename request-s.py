import requests

# 1


# def get_webpage_content(url):
#     try:
#         # Get the content of a webpage
#         response = requests.get(url)

#         # Checking the status of the response
#         response.raise_for_status()

#         # Displaying the page title
#         print("Page title:", response.headers['Content-Type'])

#         # Print the first 100 characters of the page content
#         print("First 100 characters of content:")
#         print(response.text[:100])

#     except requests.exceptions.RequestException as e:
#         print("Error retrieving page:", e)


# # Set the URL of your web page
# url = "https://www.google.com.ua/"

# # Calling a function to get and display page content
# get_webpage_content(url)
##########################################

# 2
def send_request_to_nonexistent_resource(url):
    try:
        # Send a request to a non-existent resource
        response = requests.get(url)

        # Check the status of the response
        response.raise_for_status()

        # If the response status does not indicate an error, print the content
        print("Resource content:")
        print(response.text)

    except requests.exceptions.HTTPError as http_err:
        # Handling HTTP errors
        print(f"HTTP Error: {http_err}")
    except requests.exceptions.RequestException as req_err:
        # Handling other errors
        print(f"Request Error: {req_err}")


# Set a non-existent URL
url = "https://www.example.com/nonexistent-resource"

# Call the function to send the request and handle errors
send_request_to_nonexistent_resource(url)
