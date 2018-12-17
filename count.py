import xlrd
from collections import Counter

def FindDuplicates(in_list):
    counts = Counter(in_list)
    two_or_more = [item for item, count in counts.items() if count >= 2]
    print (two_or_more)
#     print Counter(two_or_more)
    return len(two_or_more) > 0

workbook = xlrd.open_workbook(r"C:\Users\Vizi User34\Desktop\EN.JSON.xlsx")
sheet = workbook.sheet_by_index(0)
col_a = [sheet.row(row)[1].value for row in range(sheet.nrows)] # Read in all rows
print('Duplicate Values : ') 
print (FindDuplicates(col_a))
print('All values in Row',Counter(col_a))