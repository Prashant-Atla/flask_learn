import argparse
import requests
import csv
import os

def save_to_csv(data, csv_file='response_data.csv'):
    """Saves JSON data to a CSV file."""
    try:
        # If the data is a list of dictionaries
        if isinstance(data, list) and len(data) > 0:
            keys = data[0].keys()  # Extract keys from the first dictionary
            with open(csv_file, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)  # Write all rows
            print(f"Data saved to {csv_file}")
        
        # If the data is a single dictionary
        elif isinstance(data, dict):
            with open(csv_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data.keys())  # Write the header (keys)
                writer.writerow(data.values())  # Write the values (data)
            print(f"Data saved to {csv_file}")
        
        # If the data is not suitable for CSV
        else:
            print("Response data is not in a format suitable for CSV.")
    
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

def fetch_and_print(url):
    """Fetches data from a URL and prints details, saving response to CSV if applicable."""
    try:
        # Make the GET request
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Print the response details
        print('Status Code:', response.status_code)
        print('Headers:')
        for key, value in response.headers.items():
            print(f'{key}: {value}')
        print('Response Body:')
        try:
            # Try to decode the JSON response
            response_data = response.json()
            print(response_data)  # Print the JSON data for debugging
            
            # Save the response data to CSV
            save_to_csv(response_data)
        except ValueError:
            # If the response is not JSON, print it as plain text
            print("Response is not in JSON format:")
            print(response.text)

    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")

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

