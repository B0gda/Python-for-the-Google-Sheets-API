# Python Quickstart
- A simple Python command-line application that makes requests to the Google Sheets API.
---
## Prerequisites
To run this quickstart, you need the following prerequisites:
- Python 2.6 or greater.
- The pip package management tool
- A Google Cloud Platform project with the API enabled. To create a project and enable an API, refer to [Create a project and enable the API.](https://developers.google.com/workspace/guides/create-project)
> Note: For this quickstart, you are enabling the "Google Sheets API".
- Authorization credentials for a desktop application. To learn how to create credentials for a desktop application, refer to [Create credentials.](https://developers.google.com/workspace/guides/create-credentials)
A Google account.
---
## Install the Google client library
To install the Google client library for Python, run the following command:

`pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

---
## Run
From the command-line, execute the following command:

`python main.py`

*optional*. If this is your first time running the sample, the sample opens a new window prompting you to authorize access to your data:

If you are not already signed in to your Google account, you are prompted to sign in. If you are signed in to multiple Google accounts, you are asked to select one account to use for the authorization.
> Note: Authorization information is stored on the file system, so subsequent executions don't prompt for authorization.

**Click Accept.** The app is authorized to access your data.
