#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 16:12:26 2022

@author: goharshoukat


This script will sequentially perform several checks on different locations
of the caisson to determine if the design passes checks

Feeds into the Foundation_characteristic

This script is used to calculte the eccentricity checks
"""
import numpy as np
def eccentricity(input_cache, calc_cache, cap_cache, mooring_cache):
    #Inputs
    #input_cache : {}  : dictioinary with input cache    
    #calc_cache  : {}  : dictionary with precalculations
    #cap_cache  : {}  : dictionary with capacity conversions
    #mooring_cache : {} : inputs from mooring calcculations
    
    #output
    #returns an outpyt vector of boolean. True if condition is satisfied. 
    
    #checks are only performed if solution converges in precalcs, otherwise
    #the check passes as Hd and Vd would be zero and less than 1
    if calc_cache['Ta'] != 0:
        Hd = calc_cache['Ta'] * np.cos(calc_cache['theta_a'])
        Vd = calc_cache['Ta'] * np.sin(calc_cache['theta_a'])
        
        a = input_cache['L'] / calc_cache['D'] + 0.5
        b = input_cache['L'] / (3 * calc_cache['D']) + 4.5

        return ((Hd/mooring_cache['Huls'])**a + (Vd / mooring_cache['Vuls'])**b ) < 1
    else:
        return True