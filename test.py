import csv 

def mycsv_reader(csv_reader): 
  while True: 
    try: 
      yield next(csv_reader) 
    except csv.Error: 
      # error handling what you want.
      pass
    continue 
  return
     
if __name__ == '__main__': 
    reader = mycsv_reader(csv.reader(open('/Users/mazen/Desktop/python/doc.csv', 'rU')))
    for line in reader:
        print(line)
        