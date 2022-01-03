import math , numpy
from matplotlib.pyplot import axis, title
import matplotlib.pylab as plt
from lagrange import Lagrange
from wenti_1 import wenti_1 as func_analis

def dev_together( data_x_graph, dev_list_proc_graph1, dev_list_proc_graph, title='[-5,5]-blue [-1,1]-red ', axis=[-10,20,-1,20]):
    plt.axis(axis)
    plt.title(title)
    plt.xlabel('x value', color='gray')
    plt.ylabel('absolute deviation',color='gray')
    plt.plot(data_x_graph,dev_list_proc_graph1,'red')
    plt.plot(data_x_graph,dev_list_proc_graph,'blue')
    plt.grid(True)
    plt.show()

def wenti_2(n, qujian=5 , x_list=[], qujian1=1, x_list1=[], title='',func = lambda x: math.e**x , axis=[-10,20,-1,20])->None:
        dev_graph_all=[]
        data_x_gr = list(numpy.linspace(-10,20,100000))
        real_y_gr = [func(x) for x in data_x_gr]
        if len(x_list)==0:
            x_list = list(numpy.linspace(-qujian, qujian, n))
            x_list1 = list(numpy.linspace(-qujian1, qujian1, n))
            
        y_list = [func(x) for x in x_list]
        y_list1 = [func(x) for x in x_list1]
        dev_graph = []
        dev_graph1 = []
        interpolated_y_gr = [Lagrange(x_list,y_list,x) for x in data_x_gr]
        dev_graph += [abs((real_y_gr[i]-interpolated_y_gr[i])/real_y_gr[i]) for i in range(len(data_x_gr))]
        interpolated_y_gr1 = [Lagrange(x_list1,y_list1,x) for x in data_x_gr]
        dev_graph1 += [abs((real_y_gr[i]-interpolated_y_gr1[i])/real_y_gr[i]) for i in range(len(data_x_gr))]
        dev_together(data_x_gr,dev_graph1,dev_graph, title, axis=axis)
        dev_graph_all+=dev_graph

if __name__=="__main__":
    #func_analis([-0.95,-0.05,0.05,0.95], 1,)
    #func_analis(data_x=[-4.75,-0.25,0.25,4.75], qujian=5, func=lambda x: math.e**x, title_func="math.e**x")
    func_analis(data_x=[-4.75,-0.25,0.25,4.75], qujian=1, func=lambda x: math.e**x, title_func="math.e**x")
    for n in [5, 10, 20]:
        pass
        #wenti_2(n, func = lambda x: 1/(1 + x**2))
    for n in [5,10,20]:
        pass
        #wenti_2(n, func= lambda x: math.e**x)