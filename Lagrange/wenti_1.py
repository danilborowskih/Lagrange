import math , numpy
import matplotlib.pylab as plt
from lagrange import Lagrange
from decimal import Decimal, getcontext

def show_func_graph_gr(data_x, interpolated_y, real_y, n, title_func, interpolated_y_graph, real_y_graph, data_x_graph):
        plt.axis([-10,10,-10,110])
        plt.title(f'lagrange interpolation with n = {n} initial points '+title_func+' \n (blue- interpolated y, red- real y)')
        plt.xlabel('x value', color='black')
        plt.ylabel('y value',color='black')
        plt.plot(data_x,interpolated_y,'bo')
        plt.plot(data_x_graph,interpolated_y_graph,'blue')
        plt.plot(data_x,real_y,'ro')
        plt.plot(data_x_graph,real_y_graph,'red')
        for i in range(len(interpolated_y)):
            plt.text(data_x[i],interpolated_y[i],f'%.11f'%(interpolated_y[i]))
        for i in range(len(data_x)):
            plt.text(data_x[i],real_y[i],f'%.11f'%(real_y[i]))
        plt.grid(True)
        plt.show()

def show_deviation_procent_gr(data_x,deviation_list_proc, data_x_graph, dev_list_proc_graph, nado_list)->None:
    print(len(data_x_graph), len(dev_list_proc_graph))
    for nado in nado_list:
        plt.axis([-10,10,-10,10])
        plt.title('graph of deviation of the value interpolated by the Lagrange method \nfrom the real value of the function (5-blue, 10-red, 20-green)')
        plt.xlabel('x value', color='gray')
        plt.ylabel('absolute deviation',color='gray')
        l_th=len(data_x)
        nuzh=1
        for i,k,c,d in ([0,l_th,'bo','blue'],[l_th,2*l_th,'ro','red'],[2*l_th,3*l_th,'go','green']):
            if nuzh==nado:
                dev_list_proc = deviation_list_proc[i:k]
                plt.plot(data_x,(dev_list_proc),c)
                for b in range(len(dev_list_proc)):
                    plt.text(data_x[b],dev_list_proc[b],f'%.9f'%(dev_list_proc[b]))
            nuzh+=1
        
        nuzh=1
        l_th_gr = len(data_x_graph)
        for i,k,c,d in ([0,l_th_gr,'bo','blue'],[l_th_gr,2*l_th_gr,'ro','red'],[2*l_th_gr,3*l_th_gr,'go','green']):
            if nado == nuzh:
                dev_list_proc_gr = dev_list_proc_graph[i:k]
                plt.plot(data_x_graph,(dev_list_proc_gr),d)
            nuzh+=1
        plt.grid(True)
        plt.show()

def wenti_1(data_x, qujian, nado_list=[1,2,3], func = lambda x: 1/(1+x**2), title_func="1/(1+x**2")->None:
    deviation_list_proc=[]
    n_list = [20,]
    real_y = [func(x) for x in data_x]
    dev_graph = data_x_gr = []
    data_x_gr = list(numpy.linspace(-10,10,1000))
    real_y_gr = [func(x) for x in data_x_gr]
    for n in n_list:
        x_list = list(numpy.linspace(-qujian,qujian,n))#[-5+k*h for k in range(n)]
        y_list = [func(x) for x in x_list]
        interpolated_y = [ Lagrange(x_list, y_list, x) for x in data_x]
        for i in range(len(data_x)):
            deviation_proc = abs((real_y[i]-interpolated_y[i])/real_y[i])
            deviation_list_proc += [(deviation_proc)]
            print(data_x[i],'%.10f' %real_y[i], '%.10f' %interpolated_y[i], '%.17f'%deviation_proc, )
        
        interpolated_y_gr = [Lagrange(x_list,y_list,x) for x in data_x_gr]
        dev_graph += [abs((real_y_gr[i]-interpolated_y_gr[i])/real_y_gr[i]) for i in range(len(data_x_gr))]
        show_func_graph_gr(data_x,interpolated_y, real_y, n, title_func, interpolated_y_gr, real_y_gr, data_x_gr)
        
    show_deviation_procent_gr(data_x,deviation_list_proc, data_x_gr, dev_graph, nado_list)

if __name__=='__main__':
    wenti_1([0.75,1.75,2.75,3.75,4.75], 5)
    wenti_1([-0.95, -0.05, 0.05, 0.95], 1, func = lambda x: math.e**x)