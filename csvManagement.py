import csv
import numpy as np

def csvToNumpy(file_name,training_set_len):
    X = np.zeros((training_set_len,2))
    Y=np.zeros((training_set_len,1))


    with open(file=file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|',)
        next(reader, None)  # skip the headers
        i=0
        for row in reader:
            if i == training_set_len:
                break
            X[i][0]=row[0]
            X[i][1]=row[1]
            Y[i][0]=row[2]
            i+=1
    return X,Y 





