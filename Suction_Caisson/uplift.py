#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 10:35:24 2021

@author: goharshoukat

Undrained analysis for uplift (tension on anchor based)

This script will sequentially perform several checks on different locations
of the caisson to determine if the design passes checks

Feeds into the Foundation_characteristics

Uplift calculations using OWA commented out

New uplift calculations using DTOcean document put in here


#uplift and lateral checks are incldued within entricity checks. ignore this file. will be deleted.
"""
import numpy as np
import math

def uplift_check(calc_cache, cap_cache, gamma_m, gamma_f):
    #perform uplift and lateral checks
    #Inputs
    #calc__cache : {}  : dictioinary with precalucalations
    #cap_cache  : {}  : dictionary with capacity conversions
    return ()

def lateral_check(calc_cache, cap_cache, gamma_m, gamma_f):
    #perform uplift and lateral checks
    #Inputs
    #calc__cache : {}  : dictioinary with precalucalations
    #cap_cache  : {}  : dictionary with capacity conversions
    pass
    #return Vult/gamma_m >= (cap_cache['Vd'])
 
#    ===========================================================================
# def uplift(input_cache, calc_cache, soil_type, soil, cap_cache, K,
#            gamma_m, gamma_f):
# #Input
#     #soil_type  : string  : optino to choose between sand or clay
#     #soil       : {}      : dictionary with soil properties of the sub-type
#     #input_cache: dict {} : dictionary of input cache
#     #calc_cache : dict {} : dictionary of pre calculations     
#     #cap_cache  : dict {} : dictionary of capacity calculations cache
#     #K         : float : constant user specified
#     #gamma_m    : float   : ahrd coded safety factor of material
#     #gamma_f    : float   : hard coded favorable safety factor
#     
# 
#     if soil_type.lower() == 'clay':
#         """
#         uplift calculations for clay involve calculating Vult under 4 different 
#         scenarios:
#         1. Undrained clay
#         2. Cavitation at Caisson base
#         3. Cavitation under lid
#         4. Friction on the sides of caisson
#         Check the minimum value of Vult obtained and proceed witht that. 
#         """
#         #undrained
#         Vult1 = calc_cache['Wc'] + soil['Nc'] * calc_cache['Ac'] * \
#             soil['s_u'] + soil['alpha'] * math.pi * calc_cache['D'] * \
#                 calc_cache['h'] * soil['s_u']
#       
#         #cavitation at caisson base
#         Vult2 = math.pi * calc_cache['D']**2 / 4 * calc_cache['h'] * \
#             soil['gamma'] + math.pi * calc_cache['D']**2/4 * (101325 + 1000 * 
#             calc_cache['h']) + math.pi * calc_cache['D'] * soil['alpha'] * \
#                 calc_cache['h'] * soil['s_u']
#         
#         #cavitation under lid                    
#         Vult3 =  math.pi * calc_cache['D']**2/4 * (101325 + 1000 *
#            calc_cache['h']) + 2 * math.pi * calc_cache['D'] * soil['alpha'] *\
#             calc_cache['h']  * soil['s_u']
#         
#         Vult4 = 2 * math.pi * calc_cache['D'] * calc_cache['h'] * \
#             soil['alpha'] * soil['s_u']
#             
#         #for each row of values, select the lowest from the 4 and proceed
#         #with the check there
#         Vult_min = np.min([Vult1, Vult2, Vult3, Vult4], axis = 0)
#         return Vult_min/gamma_m > calc_cache['V_comma'] * gamma_f
#         
# 
#     
#     elif soil_type.lower() == 'sand':
#         """
#         uplift calculations for sand involve calculating Vult under 5 different 
#         scenarios:
#         1. Undrained 
#             a. Cavitation at footing base
#             b. Cavitation below caisson lid
#         2. Drained
#             a. Cavitation at footing base
#             b. Cavitation below caisson lid
#         3. Friction on the sides of caisson
#         Check the minimum value of Vult obtained and proceed witht that. 
#         """
#         #undrained - cavitation at footing base
#         Vult1a =  math.pi * calc_cache['D']**2 / 4 * calc_cache['h'] * soil['gamma'] + \
#             math.pi * calc_cache['D']**2/4 * (101325 + 1000 * calc_cache['h']) + math.pi * \
#                 calc_cache['D'] * soil['gamma'] * calc_cache['h'] **2/2 * K * math.tan(
#                     soil['delta'])
#          
#             
#         #undrained - cavitation below caisson lid
#         Vult1b =  math.pi * calc_cache['D']**2/4 * (101325 + 1000 * calc_cache['h']) + 2* math.pi * \
#             calc_cache['D'] * soil['gamma'] * calc_cache['h'] **2/2 * K * math.tan(
#                (soil['delta']))
#         
#         #drained - cavitation at footing base
#         Vult2a = math.pi * calc_cache['D']**2/4 * soil['gamma'] * calc_cache['h'] - \
#                 math.pi*calc_cache['D']**2/4 * 1000 * calc_cache['h'] + math.pi * \
#                     calc_cache['D'] * soil['gamma'] * calc_cache['h'] **2/2 * K * math.tan(
#                      (soil['delta']))
#         #drained - cavitation at caisson lid 
#         Vult2b = 2* math.pi * calc_cache['D'] * soil['gamma'] * calc_cache['h'] **2/2 * K \
#             * math.tan((soil['delta']))
# 
#         #Friction on the side of caissons
#         Vult3 = 2 * math.pi * calc_cache['D'] * soil['gamma'] * calc_cache['h']**2 / 2 * K * math.tan(soil['delta'])
#         
#         #find the minimum from all the above Vult calculations and 
#         #proceed with the design checker
#         Vult_min = np.min([Vult1a, Vult1b, Vult2a, Vult2b, Vult3], axis = 0)
#         
#         return Vult_min/gamma_m > calc_cache['V_comma'] * gamma_f
#         
#     else:
#         print('Incorrect Soil type selected. Please choose from sand or clay.')
#         raise ValueError
# =============================================================================
