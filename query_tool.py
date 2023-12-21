import requests
from pymongo import MongoClient

# MongoDB configuration
DATABASE_NAME = "india_ogd_data"
COLLECTION_NAME = "crude_oil_data"

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# India OGD API configuration
INDIA_OGD_API_KEY = "579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b"
INDIA_OGD_API_ENDPOINT = "https://api.data.gov.in/resource/8d3b6596-b09e-4077-aebf-425193185a5b"

def fetch_and_store_data():
    params = {
        "api-key": INDIA_OGD_API_KEY,
        "limit": 10,  # Adjust the limit as needed
        "format": "json"
    }

    try:
        response = requests.get(INDIA_OGD_API_ENDPOINT, params=params)
        response.raise_for_status()  # Raise an error for bad status codes



        data = response.json()

        if data.get("records"):
            crime_records = data["records"]

            # Insert crime records into MongoDB
            collection.insert_many(crime_records)

            print(f"Successfully fetched and stored {len(crime_records)} crime records.")
        else:
            print("No records found in the fetched data.")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    except ValueError as ve:
        print(f"Error decoding JSON: {ve}")

def query_crude_oil_data():
    print("Select the type of query:")
    print("1. Display all records")
    print("2. Display records for a specific oil company")
    print("3. Display records for a specific year")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("All crude oil records:")
        all_records = collection.find()
        for record in all_records:
            print(record)
    elif choice == "2":
        company = input("Enter the oil company name: ")
        filtered_records = collection.find({"oil_companies_": {"$regex": company, "$options": "i"}})
        print(f"Crude oil records for '{company}':")
        for record in filtered_records:
            print(record)
    elif choice == "3":
        year = input("Enter the year: ")
        filtered_records = collection.find({"year": year})
        print(f"Crude oil records for the year {year}:")
        for record in filtered_records:
            print(record)
    elif choice == "4":
        return
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    while True:
        fetch_and_store_data()

        choice = input("Do you want to query and display the fetched data? (yes/no): ")
        if choice.lower() == "yes":
            query_crude_oil_data()
        else:
            break  # Exit the loop if the user doesn't want to continue

    print("Exiting the program. Have a great day!")