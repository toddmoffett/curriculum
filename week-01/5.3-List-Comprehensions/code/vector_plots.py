import numpy as np
import matplotlib.pyplot as plt
import seaborn

def initialize_2d_plot(x_min=-1,x_max=8,y_min=-1,y_max=8):
    plot_name = plt.gca()
    plot_name.set_xlim([x_min,x_max])
    plot_name.set_ylim([y_min,y_max])
    plot_name.axhline(0, color='black')
    plot_name.axvline(0, color='black')
    return plot_name   
    
def draw_2d_scalar_multiplication(scalar,np_array,plot,color='black'):
    for i in range(scalar):
        tail = i*np_array
        draw_2d_vector(np_array,plot,i*np_array, color=color)
        
def draw_2d_vector(np_array,plot,tail=np.array([0,0]), color='black'):
    u_1 = np_array[0]
    u_2 = np_array[1]
    tail_1 = tail[0]
    tail_2 = tail[1]
    plot.arrow(tail_1,tail_2,u_1,u_2, head_width=0.125, head_length=0.125, color=color)

def draw_2d_vector_addition(np_array_1,np_array_2,plot, color='black'):
    u_1 = np_array_1[0]
    u_2 = np_array_1[1]
    v_1 = np_array_2[0]
    v_2 = np_array_2[1]
    plot.arrow(0,0,u_1,u_2, head_width=0.25, head_length=0.25, color=color)    
    plot.arrow(u_1,u_2,v_1,v_2, head_width=0.25, head_length=0.25, color=color) 