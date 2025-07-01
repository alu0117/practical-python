# fileparse.py
#
# Exercise 3.3
import csv
def parse_csv(filename, select = None, types = [str, int, float], has_headers = True, delimiter= ',') -> list: 
    '''
    Parse a CSV file into a list of record
    '''
    with open(filename, 'rt') as f:
        rows = csv.reader(f, delimiter=delimiter)
        indices = list(range(len(types))) #default indices if no selection
        if has_headers:
            headers = next(rows) 
            if select:
                indices = [headers.index(s) for s in select]
            else:
                select = headers
        records = []
        for row in rows:
            record = None
            if not row: #Skip rows with no data
                continue
            if has_headers:
                record = {col:func(row[ndx]) for col,ndx,func in zip(select,indices,types)}
            else:
                record = tuple([func(val) for func, val in zip(types,row)])
            records.append(record)
    return records
 