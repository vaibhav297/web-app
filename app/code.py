import xlrd
import openpyxl
import logging
def startx():
    sheet_name = ""
    list =[]
    try:
        workbook_master_data_tool = xlrd.open_workbook(r'Master_data.xlsm')
    except Exception as e:
        logging.error("please check file names and directories:")
        logging.error("Master_data.xlsx")
    try:
        for master_data in workbook_master_data_tool.sheets():
            if (master_data.name.lower()).startswith("DashBoard".lower()):
                master_data_sheet_name = master_data.name
        master_data_sheet = workbook_master_data_tool.sheet_by_name(master_data_sheet_name)
        for row_num1 in range(master_data_sheet.nrows):
            row_value1 = master_data_sheet.row_values(row_num1)
            print(row_value1)
            list.append(row_value1)

    except Exception as e:
        logging.error("please do not keep timesheet open")
        logging.error("please check file names and directories:")
        logging.error("C:\Finance Vision\Master_data.xlsx")
    return list;
temp = startx()
 
