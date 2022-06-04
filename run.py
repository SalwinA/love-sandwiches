"""Love_Sandwiches"""
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
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


def get_sales_data():
    """ Request User Data"""

    while True:
        print('Please enter the sales data from the last market.')
        print('Enter the numbers as per this example - 10,20,30,40,50,60\n')
        data_str = input('Please enter the numbers:')
        sales_data = data_str.split(',')
        if(validate_data(sales_data)):
            print('Data provided is valid.')
            break
    return sales_data


def validate_data(values):
    """Try & Except to validate user inputs
    are integers and exactly 6 numbers"""
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f'Required 6 values. You provided {len(values)}.')
    except ValueError as e:
        print(f'Invalid data: {e}. Please try again!!\n')
        return False
    return True


# def update_sales_worksheet(data):
#     """Updating sale worksheet with new values
#      provided by the user in a new row."""
#     print('Updating sales worksheet....\n')

#     sales_worksheet = SHEET.worksheet("sales")
#     sales_worksheet.append_row(data)
#     print('Sales worksheet updated successfully.\n')


def calculate_surplus_data(sales_row):
    """To calculate surplus stock of sandwiches"""
    print('Calculating surplus data....\n')
    stock = SHEET.worksheet('stock').get_all_values()
    stock_row = [int(num1) for num1 in stock[-1]]
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = stock - sales
        surplus_data.append(surplus)

    return surplus_data


# def update_surplus_worksheet(data):
#     """Updating surplus worksheet with new
#      values provided by the user in a new row."""
#     print('Updating surplus worksheet....\n')

#     surplus_worksheet = SHEET.worksheet('surplus')
#     surplus_worksheet.append_row(data)
#     print('Surplus worksheet updated successfully.\n')


def update_worksheet(data, worksheet):
    """Update worksheets with data"""    
    print(f'Updating {worksheet} worksheet...\n')
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f'{worksheet} worksheet updated successfully.\n')


def get_last_5_entries_sales():

    sales = SHEET.worksheet('sales')
   
    columns = []
    for ind in range(1, 7):
        column = sales.col_values(ind)
        columns.append(column[-5:])


return columns

def main():
    """Run all the functions"""

    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, 'sales')
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, 'surplus')


print('Welcome to Love Sandwiches automation program!!\n')
main()

get_last_5_entries_sales()