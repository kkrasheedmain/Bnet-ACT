# import gspread
#
# def check_google_sheet_auth(sheet_name):
#     try:
#         gc = gspread.service_account(filename="credentials.json")
#         gsheet = gc.open_by_key("1BvvG1GkQbhbHmgCN4cplU6R6qlykcDz6Cw_UpneB8FE")
#         ws = gsheet.worksheet(sheet_name)
#         # Optional test read (stronger check)
#         ws.acell("A1").value
#         # Get actual used row count (not empty rows)
#         rows = len(ws.get_all_values())
#         return rows  # ✅ authenticated → number of rows
#
#     except Exception as e:
#         print("Google Sheet Auth Error:", e)
#         return 0  # ❌ not authenticated
#

###################################
#
# import gspread
#
# def get_sheet_row_count(sheet_name):
#     try:
#         gc = gspread.service_account(filename="credentials.json")
#         gsheet = gc.open_by_key("1BvvG1GkQbhbHmgCN4cplU6R6qlykcDz6Cw_UpneB8FE")
#         ws = gsheet.worksheet(sheet_name)
#
#         # Strong auth check
#         ws.acell("A1").value
#
#         # Count actual used rows (Column A based)
#         rows = len(ws.col_values(1))
#         return rows
#
#     except Exception as e:
#         print("Google Sheet Error:", e)
#         return -1   # clearer failure signal

#############################

import gspread

SHEET_KEY = "1BvvG1GkQbhbHmgCN4cplU6R6qlykcDz6Cw_UpneB8FE"

def append_to_google_sheet(sheet_name, data_array):
    try:
        # --- Validation ---
        gc = gspread.service_account(filename="credentials.json")
        gsheet = gc.open_by_key(SHEET_KEY)
        ws = gsheet.worksheet(sheet_name)

        # Strong auth + permission check
        ws.acell("A1").value

        # Get current used row count (Column A)
        current_rows = len(ws.col_values(1))

        # New row number
        row_number = current_rows + 1

        # Insert row number at the beginning
        row_data = [row_number] + data_array

        # --- Append row ---
        ws.append_row(row_data, value_input_option="USER_ENTERED")

        return True

    except Exception as e:
        print("Google Sheet Append Error:", e)
        return False



