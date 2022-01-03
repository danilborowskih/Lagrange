import numpy as np
import math as m
from lagrange import Lagrange
from wenti_1 import show_func_graph_gr
from wenti_2 import wenti_2 as graphs_comprasion
def Chebishev_root(n, qujian=1) -> list:
    cheb_list = [ qujian*m.cos( np.float64((2*k + 1)*m.pi/( 2*((n-1) + 1))) ) for k in range(0, n) ]
    return cheb_list

def max_deiation_in_range(n, start=0.9, end=0.98, func= lambda x: 1/(1+x**2),):
    x_list = Chebishev_root(n, )
    y_list =[func(x) for x in x_list]
    x_for_deviation=list(numpy.linspace(start, end,1000))
    y_real = [func(x) for x in x_for_deviation]
    y_interpolated=[ Lagrange(x_list, y_list, x) for x in x_for_deviation]
    deviation_list=[abs((y_real[i]-y_interpolated[i])/y_real[i]) for i in range(len(y_real))]
    return max(deviation_list)

def wenti_3(n=5, qujian=1, x_for_interpolation=[-0.95,-0.05,0.05,0.95], func = lambda x: 1/(1+x**2), title="1/(x**2+1)"):
    x_list = Chebishev_root(n, qujian)
    y_list = [func(x) for x in x_list]
    y_from_interpolation=[Lagrange(x_list, y_list, x) for x in x_for_interpolation]
    real_y = [func(x) for x in x_for_interpolation]
    x_for_graphik = Chebishev_root(100000, 2)
    interpolated_y_for_graphik = [Lagrange(x_list, y_list, x) for x in x_for_graphik]
    real_y_for_graphik = [func(x) for x in x_for_graphik]
    return_list=[]
    if False:
        for i in range(4):
            return_list+=[[ x_for_interpolation[i], real_y[i], y_from_interpolation[i], abs(( y_from_interpolation[i]-real_y[i])/real_y[i])]]
        return return_list

    show_func_graph_gr(x_for_interpolation, y_from_interpolation, real_y, n, title, interpolated_y_for_graphik, real_y_for_graphik, x_for_graphik)

if __name__=="__main__":
    for n in [ 10, 20]:
        #graphs_comprasion(n=n, qujian=1, x_list= Chebishev_root(n), qujian1=1, x_list1= list(np.linspace(-1, 1, n)), 
        #title='Chebyshev polinoms root -blue ', func= lambda x: m.e**x, axis=[-3, 5, 0, 1])
        wenti_3(n, func=lambda x: m.e**x, title="e**x")
        

