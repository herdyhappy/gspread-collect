#!/usr/bin/env python
# coding: utf-8

# In[1]:


import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import os


# In[2]:


# Google Sheets API Setup
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDENTIALS_PATH = "path/to/credentials.json"  # Update this with the actual path to your JSON file


# In[3]:


def fetch_google_sheets_data(sheet_id, worksheet_name):
    """Fetch data from Google Sheets using Sheet ID and return as a Pandas DataFrame."""
    try:
        # Authenticate using credentials from file
        creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_PATH, SCOPE)
        client = gspread.authorize(creds)

        # Open the Google Sheet by ID
        sheet = client.open_by_key(sheet_id)
        worksheet = sheet.worksheet(worksheet_name)

        # Get all data
        data = worksheet.get_all_records()

        # Convert to DataFrame
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None

def save_to_csv(df, filename="output.csv"):
    """Save DataFrame to a CSV file."""
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    SHEET_ID = "your_google_sheet_id"  # Replace with your actual Google Sheet ID
    WORKSHEET_NAME = "Sheet1"  # Name of the worksheet tab

    # Fetch data
    df = fetch_google_sheets_data(SHEET_ID, WORKSHEET_NAME)

    if df is not None:
        print(df.head(5))  # Preview first 5 rows
        print(df.tail(5))  # Preview last 5 rows
        save_to_csv(df, "google_sheets_data.csv")


# In[ ]:




