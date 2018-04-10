from xlrd import open_workbook

def parseData(fileName, sheetName, start):

    book = open_workbook(fileName)

    for sheet in book.sheets():
        
        if sheet.name == sheetName:

            col_names = sheet.row(start)

            data = {}

            for row in range(start + 1, sheet.nrows):
                
                obj = {}

                for header, col in zip(col_names, range(sheet.ncols)):
                    
                    value  = sheet.cell(row, col).value
                    
                    obj[header.value] = value

                targetName = obj['Target Name']

                group = data.get(targetName)

                if group == None:
                    group = []
                    data[targetName] = group

                group.append(obj)
            
            return data

print(parseData('data.xls', 'Results', 47))
