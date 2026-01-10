import gspread

def check_google_sheet_auth():
    try:
        gc = gspread.service_account(filename="credentials.json")
        sheet = gc.open_by_key("1BvvG1GkQbhbHmgCN4cplU6R6qlykcDz6Cw_UpneB8FE")
        ws = sheet.worksheet("Sheet1")
        # Optional test read (stronger check)
        ws.acell("A1").value
        # Get actual used row count (not empty rows)
        rows = len(ws.get_all_values())
        return rows  # ✅ authenticated → number of rows

    except Exception as e:
        print("Google Sheet Auth Error:", e)
        return 0  # ❌ not authenticated


