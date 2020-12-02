import xlrd
import pandas as pd

def parse():
    print('In parse script')
    loc = 'App/productcatglisting.xls'
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    num_cols = sheet.ncols

    prod_dict = {'Code':[],'Product Name': [],'Category':[],'Supplier Cost Price':[],'Supplier':[],'QoH':[],
    'Stock Unit':[],'Unit Retail':[],'Total Retail Price':[]}

    cell = []

    #cell types
    #0 - empty string
    #1 - unicode string
    #2 - float
    for row_idx in range(1, sheet.nrows - 1):
        #print ('-'*40)
        #print ('Row: %s' % row_idx)

        for col_idx in range(0, num_cols - 1):
            cell_obj = sheet.cell(row_idx, col_idx)
            cell_val = sheet.cell_value(row_idx, col_idx) 
            cell_type = sheet.cell_type(row_idx, col_idx)  
            #print ('Column: [%s] value: [%s]' % (col_idx, cell_obj))
            #print(cell_val,cell_type)
            if(col_idx == 0 and cell_val != 'Code' and cell_type != 2):
                #print('Category:',cell_val)
                break
            elif(cell_val == 'Code'):
                break
            else:
                #print ('Column: [%s] value: [%s]' % (col_idx, cell_obj))
                cell.append(cell_val)

        #print(cell)
        if cell:
            prod_dict['Code'].append(cell[0])
            prod_dict['Product Name'].append(cell[1])
            prod_dict['Category'].append(cell[2])
            prod_dict['Supplier Cost Price'].append(cell[3])
            prod_dict['Supplier'].append(cell[4])
            prod_dict['QoH'].append(cell[5])
            prod_dict['Stock Unit'].append(cell[6])
            prod_dict['Unit Retail'].append(cell[7])
            prod_dict['Total Retail Price'].append(cell[8])

        cell = []
    
    df = pd.DataFrame(data=prod_dict)
    #print(df)

    #for row, col in df.iterrows():
     #   print('Row Index:{}'.format(row))
      #  print('Column:\n{}\n'.format(col))

    dict = df.to_numpy().tolist()
    #print(dict)

    return dict