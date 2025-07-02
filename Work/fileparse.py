# fileparse.py
#
# Exercise 3.3
import csv
def parse_csv(f, select = None, types = [str, int, float], has_headers = True, delimiter= ',', silence_errors = True) -> list: 
    '''
    Parse a CSV file into a list of record
    '''
    if isinstance(f, str):
        f = open(f, 'rt')
        
    if select and not has_headers:
        raise RuntimeError("select arguement requires column headers")
    
    indices = list(range(len(types))) #default indices if no selection
    rows = csv.reader(f)
    if has_headers:
        headers = next(rows) 
        if select:
            indices = [headers.index(s) for s in select]
        else:
            select = headers
    records = []
    for row_n, row in enumerate(rows, start = 1):
        record = None
        if not row: #Skip rows with no data
            continue
        try:
            if has_headers:
                record = {col:func(row[ndx]) for col,ndx,func in zip(select,indices,types)}
            else:
                record = tuple([func(val) for func, val in zip(types,row)])
        except ValueError as v:
            if not silence_errors:
                print(f'Row {row_n}: Couldn\'t convert {row}')
                print(f'Row {row_n}: Reason {v}')
        records.append(record)
    if not f.close:
        f.close()
    return records
 
'''if __name__ == '__main__':
    port = parse_csv('Data/portfolio.csv',types = [str,int,float])
    print(port)'''