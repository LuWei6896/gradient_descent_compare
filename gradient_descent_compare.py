#!/usr/bin/env python
# encoding: utf-8
'''
@author: wendell
@license: (C) Copyright 2018-2022, Node Supply Chain Manager Corporation Limited.
@contact:
@software: wendell
@file: .py
@time: 18-10-26 下午2:10
@desc:
'''

import random
import numpy as np
import time


def gradient_descent():
    time_begin = time.time()
    input_x = [[1, 4], [2, 5], [5, 1], [4, 2]]
    y = [19, 26, 19, 20]
    theta = [1, 1]
    loss = 10
    step_size = 0.001
    eps = 0.0001
    max_iters = 225
    error = 0
    iter_counter = 0
    #global loss;global iter_counter;global input_x;global y;global theta;global eps;global error;global step_size;global max_iters
    while(loss>eps and iter_counter<max_iters):
        loss =0
        for i in range(4):
            predict_y= theta[0]*input_x[i][0] +theta[1]*input_x[i][1]
            theta[0] = theta[0] - step_size*(predict_y-y[i])*input_x[i][0]
            theta[1] = theta[1] - step_size*(predict_y-y[i])*input_x[i][1]
        for i in range(4):
            predict_y = theta[0]*input_x[i][0] + theta[1]*input_x[i][1]
            error = 0.5*np.square(predict_y-y[i])
            loss =loss +error
        iter_counter +=1
        #print('iter_counter',iter_counter)
        #print('loss',loss)


    print('final iter_counter',iter_counter)
    print('final loss',loss)
    print('final theta',theta)
    print('total time',time.time()-time_begin)

def gradient_descent_random():
    time_begin = time.time()
    input_x = [[1, 4], [2, 5], [5, 1], [4, 2]]
    y = [19, 26, 19, 20]
    theta = [1, 1]
    loss = 10
    step_size = 0.001
    eps = 0.0001
    max_iters = 225
    error = 0
    iter_counter = 0
    #global loss;global iter_counter;global input_x;global y;global theta;global eps;global error;global step_size;global max_iters
    while(loss>eps and iter_counter<max_iters):
        loss =0
        i = random.randint(0,3)
        predict_y = theta[0]*input_x[i][0] + theta[1]*input_x[i][1]
        theta[0] = theta[0] - step_size*(predict_y-y[i])*input_x[i][0]
        theta[1] = theta[1] - step_size*(predict_y-y[i])*input_x[i][1]
        for i in range(4):
            predict_y_advance = theta[0]*input_x[i][0] + theta[1]*input_x[i][1]
            error = 0.5*np.square((predict_y_advance-y[i]))
            loss= loss + error
        iter_counter += 1
        #print('iter_counter',iter_counter)
        #print('current loss',loss)
    print('final iter_counter',iter_counter)
    print('final loss',loss)
    print('final theta',theta)
    print('total time',time.time()-time_begin)


def gradient_descent_bath():
    time_begin = time.time()
    input_x = [[1, 4], [2, 5], [5, 1], [4, 2]]
    y = [19, 26, 19, 20]
    theta = [1, 1]
    loss = 10
    step_size = 0.001
    eps = 0.0001
    max_iters = 225
    error = 0
    iter_counter = 0
    while(loss>eps and iter_counter<max_iters):
        loss = 0
        i = random.randint(0,3)
        j=(i+1)%4

        predict_y = theta[0]*input_x[i][0] + theta[1]*input_x[i][1]
        theta[0] = theta[0] -step_size*(predict_y-y[i])*input_x[i][0]
        theta[1] = theta[1]-step_size*(predict_y-y[i])*input_x[i][1]

        predict_y2 = theta[0]*input_x[j][0] + theta[1]*input_x[j][1]
        theta[0] = theta[0] - step_size*(predict_y2-y[j])*input_x[j][0]
        theta[1] = theta[1] - step_size*(predict_y2-y[j])*input_x[j][1]

        for i in range(4):
            predict_y_advance = theta[0]*input_x[i][0] + theta[1]*input_x[i][1]
            error = 0.5*np.square((predict_y_advance-y[i]))
            loss = loss+error
        iter_counter +=1
        #print('iter_counter',iter_counter)

    print('final iter_counter',iter_counter)
    print('final loss',loss)
    print('final theta',theta)
    print('total time',time.time()-time_begin)


if __name__=='__main__':
    print('gradient_descent method')
    gradient_descent()
    print('---------*-------------')
    print('gradient_descent_random method')
    gradient_descent_random()
    print('---------*-------------')
    print('gradient_descent_bath method')
    gradient_descent_bath()
