import xlrd
import openpyxl
import logging
import datetime
from datetime import datetime

try:
    workbook_master_data_tool = xlrd.open_workbook(r'Master_data.xlsm')
except Exception as e:
    logging.error("please check file names and directories:")
    logging.error("../Master_data.xlsx")

try:
    def days_between(start_datee, end_date):
        start_datee = datetime.strptime(start_datee, "%d-%m-%Y")
        end_date = datetime.strptime(end_date, "%d-%m-%Y")
        return (end_date - start_datee).days
except Exception as e:
    print(" ")
try:
    def find_week(date):
        try:
            pcb_sheet = workbook_master_data_tool.sheet_by_name('PCB Calendar')
        except Exception as e:
            print("please check the pcb worksheet with name PCB Calendar_22-Jun-2020 11_50_ is present in PCB Calendar_22-Jun-2020 11_50_05.xlsx")

        for row_num1 in range(pcb_sheet.nrows):
            row_value1 = pcb_sheet.row_values(row_num1)
            print (row_value1)
            if row_num1 == 0:
                for x in range(len(row_value1)):
                    if row_value1[x].lower().strip() == "Month".lower():
                        month_index = x
                    if row_value1[x].lower().replace(" ", "").strip() == "StartDate".lower():
                        start_date_index = x
                    if row_value1[x].lower().replace(" ", "").strip() == "EndDate".lower():
                        end_date_index = x
            if row_num1 > 0:

                month = row_value1[month_index]
                months_ab = datetime(*xlrd.xldate_as_tuple(month, 0)).strftime("%b-%y")

                if months_ab == str(date):
                    start_date = row_value1[start_date_index]
                    end_date = row_value1[end_date_index]
                    start_date = datetime(*xlrd.xldate_as_tuple(start_date, 0)).strftime("%d-%m-%Y")
                    end_date = datetime(*xlrd.xldate_as_tuple(end_date, 0)).strftime("%d-%m-%Y")
                    total_days = days_between(start_date, end_date) + 1
                    total_weeks = total_days / 7
                    return total_weeks
except Exception as e:
    print("please check the month in row revenue column master data sheet")

def startx():

    global mth_list,len1,len2
    mth_list = []
    list = []
    sheet_name = ""

    try:
        for master_data in workbook_master_data_tool.sheets():
            if (master_data.name.lower()).startswith("DashBoard".lower()):
                master_data_sheet_name = master_data.name
        master_data_sheet = workbook_master_data_tool.sheet_by_name(master_data_sheet_name)
        for row_num1 in range(master_data_sheet.nrows):
            len2= master_data_sheet.nrows
            row_value1 = master_data_sheet.row_values(row_num1)
            print(row_value1)
            list.append(row_value1)

            if row_num1 == 0:
                len1 = len(row_value1)
                for x in range(len(row_value1)):
                    if "'" in row_value1[x]:
                        mth_list.append(row_value1[x])
    except Exception as e:
        logging.error("please do not keep timesheet open")
        logging.error("please check file names and directories:")
        logging.error("C:\Finance Vision\Master_data.xlsx")
    return list;
temp = startx()


month_idx = []
month_val =[]

week_list = []
actual_list =[]
len_mth=len(mth_list)
for x in range(len(mth_list)):
    month,year = mth_list[x].split("'")
    year = datetime.strptime(year, "%Y").strftime("%y")
    date = month+"-"+year
    week = find_week(date)
    total =int(week) + 5
    total_actual = int(week)+3
    week_list.append(total)
    actual_list.append(total_actual)