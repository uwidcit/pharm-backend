import pandas

#use if no headers in csv file
#df = pandas.read_csv('products.csv',
#           header=0,
#           names=['id','name','description','image','unit_price'])

#for small csv
#df = pandas.read_csv('products.csv')
#print(df)

#if you want to do something with each chunk as it is read
#for chunk in pandas.read_csv('products.csv',chunksize=chunksize, iterator=True):
#    print(chunk) #your code here

#for large csv read in chunks
def parse():
    print('Parse csv script')
    chunksize = 5
    chunk = pandas.read_csv('App/products.csv',chunksize=chunksize, iterator=True)
    df = pandas.concat(chunk,ignore_index=True)
    return(df.to_numpy().tolist())
    #print(df)

    #for row, col in df.iterrows():
        #print('Row Index:{}'.format(row))
        #print('Column:\n{}\n'.format(col))