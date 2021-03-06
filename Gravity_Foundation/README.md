# Gravity Based Foundation Modelling
Gravity based foundation (GBF) module of the Selkie Project makes use of classical object oriented programing approach. Several different functions, seperately written, feed into the main class as pythonic descriptors (descriptors is an attribute of Python that can be viewed in more detail using Python's own documentation.) 


Fig. 1 shows the different functions which are also the objects within the main class. The figure provides a description of the functions that make up the class. Each function within the class provides furhter description about their utility, inputs and outputs. They are also highlighted in this documentation.  


Included within the documentation is a designer script which provides the user a sample script deploying the current algorithm. The user, without jumping into the code or its details, can simply alter the input parameters stated in the designer script. Care has to be taken about ensuring unit similarity, otherwise, the code will not function as desired. The default units for each input parameter is stated in the designer script and in each individual class object. Furthermore, a detailed breakdown of the inputs, outputs and their respective units, datatypes are explained in this document as well. 


![](images/work_flow.jpg)


*Figure 1 shows the code architecture - the individual scripts that make up the complete algorithm, the objects that make use of these external functions and finally the class (module)*


The algorithm only makes use of built-in/standardy python libraries. No additional installations are required. 


## Version 0.00:
Warning: This version is not a stable released version. It is work in progress. 

## Functions:

We will cover each function available within the GBF class, specify the inputs and outputs for them and the datatypes.


This class takes in a number of arguments. All these make it extremely important that each argument passed down is referenced with the variable definition as defined in the class.


class Foundation_Definition(): A Foundation_Definition instance is a collection of dimensions, groups, variables and attributes that together define the process to design a GBF definition.

Foundation_Definition():


	- __init__(self, weight_concrete, weight_slag, slope, device_geometry, SF):
This is the initialization function. To declare an instance of the class Foundation_Definition, call the class from the library foundation_characterisitcs  and pass on the directory containing the datafiles. To declare an isntance of this class, the following inputs are required:

		- weight_concrete : float   : kN/m**3
       		- weight_slab     : float   : kN/m**3
       		- slope           : float   : degrees
        	- device_geometry : float   : unspecified, Pault to confirm
		- SF     	  : float   : safety factor for beariing capacity



	- def drained_soil(self, friction_angle, cohesion, fos, sensitivity):

This function is called to define a soil formation which is drained. The properties of a drained soil are then input here which can be accessed by the instance of that class. The following are the inputs required for this function: 

        	- friction_angle         : float : angle in degrees, obtained from lookup table. 
        	- cohesion               : float : value in kPa
        	- fos (factor of safety) : float :
        	- sensititivity          : TBD with Paul : 
    
It however, has no outputs and any property added is then accessible to the instance. 

         

	- def undrained_soil(self, friction_angle, cohesion, fos, relative_density, weight, sensitivity):

Similar to the last function, this object is called when the soil formation presents the behavior of an undrained soil. The arguments it takes are the properties of necessary to define the undrained behavior. It takes the following inputs: 

        	- friction_angle         : float : angle in degrees, obtained from lookup table. 
        	- cohesion               : float : value in kPa
        	- fos (factor of safety) : float : 
        	- relative_density       : float : %, obtained from the look-up table, user defined 
        	- Weight of soil         : float : kN/m**3, Weight of soil
        	- sensititivity          : TBD with Paul : 

It does not have any additional outputs either. All the properties input are then accessible to the instance of the class. 


	- def external_loads(self, Mxuls, Myuls, Vuls, Huls):
        	
This function needs to be called to provide external loads applicable on the foundation. These can be attributed to the wave hydrodynamics, etc. The function takes in the following four inputs:
	
		- Mxuls : float : kN-m, User-defined
        	- Myuls : float : kN-m, User-defined
        	- Vuls  : float : kN,   User-defined
        	- Huls  : float : kN,   User-defined

This function also does not have any outputs. The input values are then accessible to the other objects of the class through the instance. 

 
	- def key_calc(self, key: str):
        	
This function needs to be called to define if there is a key present in the design. Even if the key is absent, the function still needs to be called and an input given so that dimensions are calculated with the information that no key is present for the given foundation design. This function makes use of the following inputs:

        	- key : string : yes, y, all cases permitted. if yes, launches key calculations
        	- embed : string : Utility and incoorporation of this function will be provided in the future iteration. It is however, included within the code for now but performs no operation

This function has no output. The input information and the corresponding changes are then available for the life of the instance. 


	-  def eccentricity(self):
		
This function takes no additional inputs. It also has no additional outputs. Calling this function however ensures calculation of very important dimensional calculations which are required for by the design checker. This will be revised in the next iteration and included within the external loads adjustment function. 


	- def design_check(self):

Finally, the library calls the design_check function which runs 3 checks -- (1) Bearing Capacity, (2) Overturning Resistance, (3) Sliding Resistance. It however, needs no inputs. Note that this function makes use of external loads that are different from the ones calculated from slope adjustement. 

The output of this function is a pandas dataframe with several different dimensional values. Included within the dataframe is the result of the 3 checks performed.                
