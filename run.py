import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches2')

def get_sales_data():
    """
    get the saled data from user
    """
    print('Please enter the sales data from the last market')
    print('Data should be six numbers, separated by comma')
    print('ex: 00, 11, 22, 33, 44, 55\n')
    data_str = input('Enter your data here:')
    print(f'The data provided is {data_str}')
    sales_data = data_str.split(',')
    print(sales_data)
    validate_data(sales_data)

def validate_data(values):
    """
    converts into integers

    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")





get_sales_data()