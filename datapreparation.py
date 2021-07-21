import pandas as pd

dataread=pd.read_csv(r"C:/Users/ayadi/OneDrive/Desktop/2000-16-traffic-flow-england-scotland-wales/accidents_2012_to_2014.csv", usecols = ['Longitude','Latitude'])
filename = 'block'
#usecols = ['Longitude','Latitude','Accident_Severity']

#for subdivision of file, if block file is large
#filename = 'block_6_1'
#dataread=pd.read_csv(r"C:/Users/ayadi/OneDrive/Desktop/2000-16-traffic-flow-england-scotland-wales/blocks/"+filename+".csv", usecols = ['Longitude','Latitude'])

def getBoundaryPoints(data):
    return data.Longitude.min(),data.Longitude.max(),data.Latitude.min(), data.Latitude.max()

minLongitude,maxLongitude,minLatitude,maxLatitude = getBoundaryPoints(dataread)
print('--------')

#number of data division = numberOfSquares*numberOfSquares
numberOfSquares = 4
longitude_range = maxLongitude-minLongitude
latitude_range = maxLatitude - minLatitude
blocksize_long = longitude_range/numberOfSquares
blocksize_lat = latitude_range/numberOfSquares

print('lonRange,latRange,blockLong,blockLat:',longitude_range, latitude_range, blocksize_long, blocksize_lat)
print('--------')

def dataPartioning(data):    
    for i in range(numberOfSquares):
        startLongitude = minLongitude + i*blocksize_long
        endLongitude = minLongitude + (i+1)*blocksize_long
        #initialise latitude here
        for j in range(numberOfSquares):
            print('Counter: ', i, j)
            startLatitude = minLatitude + j*blocksize_lat
            endLatitude = minLatitude + (j+1)*blocksize_lat
            block = data.loc[(data['Longitude']>= startLongitude) & (data['Longitude'] < endLongitude) & (data['Latitude'] >= startLatitude) & (data['Latitude'] < endLatitude)]
            
            #block.to_csv('block_'+str(i)+'_'+str(j),sep=','+'.csv', index=False)
            #subdivision
            block.to_csv(filename+'_'+str(i)+'_'+str(j)+'.csv',sep=',', index=False)
            #return block

dataPartioning(dataread) 
print('--Completed--')


