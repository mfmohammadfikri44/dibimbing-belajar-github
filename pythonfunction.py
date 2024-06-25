import requests
import csv
from io import StringIO

def read_csv_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  #Raises an HTTPError for bad responses

        #Using StringIO to simulate a file object from the response content
        csv_data = StringIO(response.text)

        #Reading CSV data using csv.reader
        csv_reader = csv.reader(csv_data)
        
        #Process the CSV data (example: printing each row)
        for row in csv_reader:
            print(row)  #Replace with your desired processing logic
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

#URL of the CSV file
url = "https://support.staffbase.com/hc/en-us/article_attachments/360009197031/username.csv"

#Call the function with the URL
read_csv_from_url(url)
