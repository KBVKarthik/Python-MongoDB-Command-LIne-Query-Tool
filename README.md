# Crude Oil Data Management using MongoDB and India OGD API

This Python script manages and fetches crude oil data from the India Open Government Data (OGD) API and stores it in a MongoDB database. Additionally, it allows querying and displaying the stored data based on various criteria.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)
- `pymongo` library (`pip install pymongo`)
- MongoDB installed and running locally

## Setup

1. Install the required libraries using `pip`.
2. Ensure MongoDB is installed and running on your local machine.
3. Update the `INDIA_OGD_API_KEY` variable with your India OGD API key.
4. Modify the MongoDB configuration variables (`DATABASE_NAME`, `COLLECTION_NAME`) if needed.

## Usage

### Fetching and Storing Data

Run the script to fetch and store crude oil data from the India OGD API into your local MongoDB:

```bash
query_tool.py
```

Adjust the limit parameter in the fetch_and_store_data() function to control the number of records fetched.

## Querying Data

After fetching the data, you can query and display the stored records:

```bash

query_tool.py
```

Follow the on-screen prompts:

-Choose the type of query (display all records, records for a specific oil company, records for a specific year, or exit).
-Input relevant information based on your query choice.

## Functionality

- fetch_and_store_data(): Fetches data from the India OGD API and stores it in the specified MongoDB collection.
- query_crude_oil_data(): Allows querying the stored data based on different criteria like company name or year.
