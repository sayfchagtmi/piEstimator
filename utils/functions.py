# Import needed packages
import pyspark
import numpy as np
from time import time
from math import pi
from random import random

# function that randomly create a point inside unit circle
def is_point_inside_unit_circle(p):
    x,y = random(), random()
    return x*x + y*y < 1

# Estimate pi using spark
def pi_estimator_spark(n):
    sc = pyspark.SparkContext("local","PySpark Pi Estimator")
    sc.setLogLevel("ERROR")
    count =  sc.parallelize(range(n)) \
            .map(is_point_inside_unit_circle) \
            .reduce(lambda a, b: a + b)
    return (4*count/n)
    sc.stop()

# Estimate pi using numpy
def pi_estimator_numpy(n):
    data = np.random.uniform(-1,1, size=(n, 2))    
    inside = len(np.argwhere(np.linalg.norm(data, axis=1) < 1))
    return inside/n*4

# Generic function that take as input the simulation function and iteration number 
# and return a formatted table line to show method name, execution time, estimated 
# pi value and the deviation regarding true Pi value
def simulate(f,n):
    method = f.__name__.split("_")[-1]
    t_0 = time()
    s_pi = f(n)
    t_exec = np.round(time()-t_0, 3)
    p_ecart = abs(pi-s_pi)
    return "%12s \t|\t %12s s \t|\t %12s \t|\t %12s %s \t|" % (method,t_exec,s_pi,p_ecart*100,"%")