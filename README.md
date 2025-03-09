# gspread-collect
Collecting Data from Google Sheet

## Steps
### Enable Google Sheets API
1. Go to Google Cloud Console.
2. Create a new project.
3. Enable the Google Sheets API and Google Drive API.
4. Go to "Credentials" > "Create Credentials" > "Service Account".
5. Download the JSON key file and store it as credentials.json in your project folder.
6. Share your Google Sheet with the service account email (found in credentials.json).

### Install Dependencies
1. pip install gspread pandas oauth2client
2. 
### Address Google Sheet File
1. Update the Google Sheet ID and worksheet name in the script to match your specific Google Sheet
