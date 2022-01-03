import numpy as np
from lagrange import Lagrange
from wenti_1 import show_func_graph_gr



def wenti_4(x_list=[1,4,9], x_for_interpolation=[5, 50, 115, 185], func = lambda x: x**0.5, title="x**0.5"):
    y_list = [func(x) for x in x_list]
    y_from_interpolation=[Lagrange(x_list, y_list, x) for x in x_for_interpolation]
    real_y = [func(x) for x in x_for_interpolation]
    #x_for_graphik = np.linspace(-1,1,1000)
    #interpolated_y_for_graphik = [Lagrange(x_list, y_list, x) for x in x_for_graphik]
    #real_y_for_graphik = [func(x) for x in x_for_graphik]
    return_list=[]
    if True:
        for i in range(len(x_for_interpolation)):
            print("%.0f\t%.5f" %(x_for_interpolation[i], abs(( y_from_interpolation[i]-real_y[i])/real_y[i])))

    #show_func_graph_gr(x_for_interpolation, y_from_interpolation, real_y, n, title, interpolated_y_for_graphik, real_y_for_graphik, x_for_graphik)

if __name__=="__main__":
    for k in [1,4,9],[36,49,64],[100,121,144],[169,196,225]:
        wenti_4(x_list=k,)
        print("")
        
        

