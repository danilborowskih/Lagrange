import math , numpy as np
from lagrange import Lagrange
from wenti_3 import Chebishev_root

def greater_accuraty(data_x=[-0.95,-0.05,0.05,0.95], qujian = 1, func = lambda x: math.e**x, n=20):
    real_y = [np.float64( func(x)) for x in data_x]
    x_list=Chebishev_root(n)
    x_list2 = list(np.linspace(-qujian,qujian,n))
    y_list = [np.float64(func(x)) for x in x_list]
    y_list2 = [np.float64(func(x)) for x in x_list2]
    interpolated_y = [ np.float64(Lagrange(x_list, y_list, x)) for x in data_x]
    interpolated_y2 = [ np.float64(Lagrange(x_list2, y_list2, x)) for x in data_x]
    for i in range(len(real_y)):
        deviation_proc = np.float64(abs((real_y[i]-interpolated_y[i])/real_y[i]))
        deviation_proc2 = np.float64(abs((real_y[i]-interpolated_y2[i])/real_y[i]))
        print('%.2f\t%.17f\t%.17f\t%.3f' %(data_x[i], deviation_proc, deviation_proc2, deviation_proc/deviation_proc2),  )

for n in [5,10,20]:
    greater_accuraty( n=n, func= lambda x: 1/(x**2+1))
    print('')