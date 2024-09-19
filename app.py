import argparse
import requests

def fetch_and_print(url):
    try:
        # GET request
        response = requests.get(url)
        # Print the full response details
        print('Status Code:', response.status_code)
        print('Headers:')
        for key, value in response.headers.items():
            print(f'{key}: {value}')
        print('Response Body:')
        try:
            # Attempt to decode the JSON response
            print(response.json())
        except ValueError:
            print(response.text)
    except requests.RequestException as e:
        print(f'Error fetching the URL: {e}')

if __name__ == '__main__':
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Fetch and print details from a URL.')
    parser.add_argument(
        'url',
        type=str,
        nargs='?',  # Makes this argument optional
        default='http://localhost:5000',  # Default URL
        help='The URL to fetch the GET request from. Defaults to http://localhost:5000/your-endpoint if not provided.'
    )
    args = parser.parse_args()
    
    fetch_and_print(args.url)
