"""
    This module basically applies the batch normalization algorithm in solving
    the exploding/vanishing gradient problem by zero-centering and normalizing the
    input.
    * It does help in input changes during distribution of parameters to input 
    layers as the parameter of the previous layer changes, which is called the
    internal covariate problem (parsing parameters from a layer to another).
    
    *It does add operations to the model just before activation function of each 
    layer by zero-centering and normalizing input, then scaling and shifting 
    inputs.
    * thereby making the model learn the optimal scale and mean of the inputs for
    each layer.
    
    * inorder to zero-center and normalize, the algorithm needs to estimate the 
    input mean and standard deviation over the current mini-batch.
    
    *
"""


import numpy as np
import Exception
import warnings

class _batch_normalization:
    def __init__(self):
        """
        The Batch Normalization algorithm
        """
        return
    
    
    
    def _input_validation(self,x_data, mb):
        if isinstance(mb, int):
            validity= True
        elif isinstance(mb, float):
            mb = int(mb)
            validity = True
        else:
            validity = False
            raise('Invalid data type ' + type(mb) + 'for our batch size')
        
        # check if x_data is a list, or a numpy array of data else raise error
        if isinstance(x_data, list) or isinstance(x_data, ndarray):
            validity = True
            pass
        else:
            raise('Invalid data type for X as '+ type(X) + ' We expected X to be either a list or a numpy array of data')
            validity = False
        # check if there are no nan values else raise error
        if (np.nan in x):
            validity = False
        else:
            validity = True
            
        # check if mb is not greater than x_data shape else raise error
        if mb > x_data.shape[0]:
            validity = False
            raise("""mini-batch data size is equivalent to size of X
            both have size %ii""" % (mb))
        else:
            validity = True
            
        return validity
    
 
    
    def _get_item(self):
        return
    
    
    def __isstr__(self,value):
        return value is str
    
    
    def __len__(self,k):
        return len(k)
    
    
    def _emprical_mean(self,x_value,mb):
        """
        compute the empirical mean, evaluated over the whole mini-batch B.
        """
        value =  0
        sum_mean = value+=x_value[k] for k in range(1, mb)
        return sum_mean/mb
    
    
    
    def _compute_sd(self,x_value,emprical_mean,mb):
        """
        compute the emperical standard deviation over the whole mini-batch
        given minibatch mb and data x (data batch).
        """
        mean_difference = [pow(x_value[value] - emprical_mean,2) for value in range(1,mb)]
        return mean_difference/mb
    
    
    
    def _zero_centered_normalized_input(self, centered_input, ea,mb):
        """
        # centered_input: this is the input value that would be zero-centered 
        and normalized.
        # ea: this is a tiny number to aviod division by zero (typically 10e-5).
        This is called a SMOOTHING TERM.
        ********************************************
        This helps us to compute the normalized form of an input 'centered_input'
        and ensures it is zero-centered.
        ********************************************
        """
        emprical_mean = self._emprical_mean(centered_input,mb)
        emprical_standard_deviation = self._compute_sd(centered_input,emprical_mean, mb)
        return (centered_input - emprical_mean)/ np.square(emprical_standard_deviation + ea)
    
    
    
    def _output_batch_normalizer(self, x_value,shift_param, scaler,ea, mb):
        """
        *****************************************************************
        This outputs the batch normalized solution of a data
        Ensuring that it is the scaled and shifted version of the input
        *****************************************************************
        
        # x_value: is the value to be normalized  shifted
        #shift_param: is the shifting parameter(offset) for the layer
        # scaler: is the scaling paramter for the layer
        # ea: This is a tiny number to avoid division by zero, this is
        called the smothing term.
        """
        zero_centered_and_normalized_input = self._zero_centered_normalized_input(x_value, ea,mb)
        return scaler * x_value + zero_centered_and_normalized_input
        
        
    
if __name__ == "__main__":
    batch_normalization(sys.argv)
    

