import math , numpy
from matplotlib.pyplot import title
import matplotlib.pylab as plt
from lagrange import Lagrange

def show_deviation_procent(data_x,deviation_list_proc,)->None:
    plt.axis([-2,2,-1,3])
    #plt.title('拉格朗日法插值值与函数实际值的偏差图\nn=5- blue, n=10- red, n=20- green')
    plt.title('graph of abs deviation of the value interpolated by the Lagrange method \nfrom the real value of the function (5-blue, 10-red, 20-green)')
    plt.xlabel('x value', color='gray')
    plt.ylabel('absolute deviation',color='gray')
    l_th=len(data_x)
    for i,k,c,d in ([0,l_th,'bo','blue'],[l_th,2*l_th,'ro','red'],[2*l_th,3*l_th,'go','green']):
        dev_list_proc = deviation_list_proc[i:k]
        plt.plot(data_x,(dev_list_proc),c)
        plt.plot(data_x,(dev_list_proc),d)
        for b in range(len(dev_list_proc)):
            plt.text(data_x[b],dev_list_proc[b],f'%.7f'%(dev_list_proc[b]))
    plt.grid(True)
    plt.show()

def show_deviation_procent_gr(data_x,deviation_list_proc, data_x_graph, dev_list_proc_graph,)->None:
    print(len(data_x_graph), len(dev_list_proc_graph))
    for nado in [1,2,3]:
        plt.axis([-10,10,-10,10])
        plt.title('graph of abs deviation of the value interpolated by the Lagrange method \nfrom the real value of the function (5-blue, 10-red, 20-green)')
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

def show_func_graph_gr(data_x,interpolated_y,real_y,n,title,interpolated_y_graph,real_y_graph,data_x_graph):
        plt.axis([-10,10,-10,110])
        plt.title(f'lagrange interpolation with n = {n} initial points {title} \n (blue- interpolated y, red- real y)')
        plt.xlabel('x value', color='black')
        plt.ylabel('y value',color='black')
        plt.plot(data_x,interpolated_y,'bo')
        plt.plot(data_x_graph,interpolated_y_graph,'blue')
        plt.plot(data_x,real_y,'ro')
        plt.plot(data_x_graph,real_y_graph,'red')
        for i in range(len(interpolated_y)):
            plt.text(data_x[i],interpolated_y[i],f'%.7f'%(interpolated_y[i]))
        for i in range(len(data_x)):
            plt.text(data_x[i],real_y[i],f'%.7f'%(real_y[i]))
        plt.grid(True)
        plt.show()
def show_func_graph(data_x,interpolated_y,real_y,n,title,interpolated_y_graph,):
        plt.axis([-2,2,0,5])
        plt.title(f'lagrange interpolation with n = {n} initial points {title} \n (blue- interpolated y, red- real y)')
        plt.xlabel('x value', color='black')
        plt.ylabel('y value',color='black')
        plt.plot(data_x,interpolated_y,'bo')
        plt.plot(data_x,interpolated_y_graph,'blue')
        plt.plot(data_x,real_y,'ro')
        plt.plot(data_x, real_y,'red')
        for i in range(len(interpolated_y)):
            plt.text(data_x[i],interpolated_y[i],f'%.7f'%(interpolated_y[i]))
        for i in range(len(data_x)):
            plt.text(data_x[i],real_y[i],f'%.7f'%(real_y[i]))
        plt.grid(True)
        plt.show()

def dev_together( data_x_graph, dev_list_proc_graph1, dev_list_proc_graph,):
    plt.axis([-10,20,-1,20])
    #plt.title('拉格朗日法插值值与函数实际值的偏差图\nn=5- blue, n=10- red, n=20- green')
    plt.title('[-1,1]-blue [-5,5]-red')
    plt.xlabel('x value', color='gray')
    plt.ylabel('absolute deviation',color='gray')
    plt.plot(data_x_graph,dev_list_proc_graph1,'blue')
    plt.plot(data_x_graph,dev_list_proc_graph,'red')
    plt.grid(True)
    plt.show()


def wenti_1_1(data_x, qujian)->None:
    deviation_list_proc=[]
    n_list = [5,10,20]
    real_y = [1/(1+x**2) for x in data_x]

    #gr
    dev_graph=[]
    data_x_gr=[]
    data_x_gr = list(numpy.linspace(-10,10,1000))
    real_y_gr = [1/(1 + x**2) for x in data_x_gr]
    #gr

    for n in n_list:
        print(f"\nfor n = {n}")
        x_list = list(numpy.linspace(-qujian,qujian,n))#[-5+k*h for k in range(n)]
        y_list = [1/(1+x**2) for x in x_list]
        interpolated_y = [ Lagrange(x_list, y_list, x) for x in data_x]
        
        print("x      y        y interpolation deviation")
        for i in range(len(data_x)):
            deviation_proc = ((real_y[i]-interpolated_y[i])/real_y[i])
            deviation_list_proc += [abs(deviation_proc)]
            print(f"{data_x[i]}   %.4f   %.4f \t %.4f" %(real_y[i], interpolated_y[i], deviation_proc))
        #gr
        interpolated_y_gr = [Lagrange(x_list,y_list,x) for x in data_x_gr]
        dev_graph += [abs((real_y_gr[i]-interpolated_y_gr[i])/real_y_gr[i]) for i in range(len(data_x_gr))]
        #gr
        title = "1/(1+x**2)"
        show_func_graph_gr(data_x,interpolated_y,real_y,n,title, interpolated_y_gr, real_y_gr, data_x_gr)
    show_deviation_procent_gr(data_x,deviation_list_proc, data_x_gr, dev_graph)

wenti_1_1()

def wenti_1_2()->None:
    """第1问题第2部的解"""
    deviation_list_proc = []
    n_list = [5,10,20]
    #data_x = [-0.95,-0.05,0.05,0.95]
    data_x = [-4.75,-0.25,0.25,4.75]
    #gr
    dev_graph=[]
    data_x_gr=[]
    data_x_gr = list(numpy.linspace(-20,20,10000))
    real_y_gr = [math.e**x for x in data_x_gr]
    #gr
    for n in n_list:
        print(f"\nfor n = {n}")
        x_list = list(numpy.linspace(-5,5,n))
        y_list = [math.e**x for x in x_list]
        interpolated_y = [ Lagrange(x_list, y_list, x) for x in data_x]
        real_y = [math.e**x for x in data_x]

        print("x      y        y interpolation deviation")
        for i in range(len(data_x)):
            deviation_proc = ((real_y[i]-interpolated_y[i])/real_y[i])
            deviation_list_proc += [abs(deviation_proc)]
            print(f"{data_x[i]}   %.4f   %.4f \t %.4f" %(real_y[i], interpolated_y[i], deviation_proc))
        #gr
        interpolated_y_gr = [Lagrange(x_list,y_list,x) for x in data_x_gr]
        dev_graph += [abs((real_y_gr[i]-interpolated_y_gr[i])/real_y_gr[i]) for i in range(len(data_x_gr))]
        #gr
        title = "e**x"
        #show_func_graph(data_x,interpolated_y,real_y,n,title)
        #show_func_graph_gr(data_x,interpolated_y,real_y,n,title, interpolated_y_gr, real_y_gr, data_x_gr)
    #show_deviation_procent(data_x,deviation_list_proc)
    show_deviation_procent_gr(data_x,deviation_list_proc, data_x_gr, dev_graph)

#wenti_1_2()

def wenti_2_1()->None:
    n_list = [5,10,20]
    dev_graph_all=[]
    data_x_gr = list(numpy.linspace(-10,10,1000))
    real_y_gr = [1/(1 + x**2) for x in data_x_gr]
    for n in n_list:
        x_list = list(numpy.linspace(-5,5,n))
        y_list = [1/(1+x**2) for x in x_list]
        x_list1 = list(numpy.linspace(-1,1,n))#[-5+k*h for k in range(n)]
        y_list1 = [1/(1+x**2) for x in x_list1]
        dev_graph = []
        dev_graph1 = []
        interpolated_y_gr = [Lagrange(x_list,y_list,x) for x in data_x_gr]
        dev_graph += [abs((real_y_gr[i]-interpolated_y_gr[i])/real_y_gr[i]) for i in range(len(data_x_gr))]
        interpolated_y_gr1 = [Lagrange(x_list1,y_list1,x) for x in data_x_gr]
        dev_graph1 += [abs((real_y_gr[i]-interpolated_y_gr1[i])/real_y_gr[i]) for i in range(len(data_x_gr))]
        dev_together(data_x_gr,dev_graph,dev_graph1,)
        dev_graph_all+=dev_graph

wenti_2_1()

def wenti_2_2()->None:
    n_list = [5,10,20]
    dev_graph_all=[]
    data_x_gr = list(numpy.linspace(-10,20,10000))
    real_y_gr = [math.e**x for x in data_x_gr]
    for n in n_list:
        x_list = list(numpy.linspace(-5,5,n))
        y_list = [math.e**x for x in x_list]
        x_list1 = list(numpy.linspace(-1,1,n))#[-5+k*h for k in range(n)]
        y_list1 = [math.e**x for x in x_list1]
        dev_graph = []
        dev_graph1 = []
        interpolated_y_gr = [Lagrange(x_list,y_list,x) for x in data_x_gr]
        dev_graph += [abs((real_y_gr[i]-interpolated_y_gr[i])/real_y_gr[i]) for i in range(len(data_x_gr))]
        interpolated_y_gr1 = [Lagrange(x_list1,y_list1,x) for x in data_x_gr]
        dev_graph1 += [abs((real_y_gr[i]-interpolated_y_gr1[i])/real_y_gr[i]) for i in range(len(data_x_gr))]
        dev_together(data_x_gr,dev_graph1,dev_graph,)
        dev_graph_all+=dev_graph

wenti_2_2()