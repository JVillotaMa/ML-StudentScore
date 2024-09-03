import numpy as np
from csvManagement import csvToNumpy
from model import compute_linear
from plot import plot_init
from plot import plot_final
from Utilities import suit_np

X,Y=csvToNumpy("StudentPerformance.csv",3000)

model=compute_linear(X,Y,150)

predict_input=suit_np(100,2)



predict_output=model.predict(predict_input)

plot_final(X,Y,predict_output)
