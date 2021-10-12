import pandas as pd
import numpy as np


def normal_pdf(x,mean,sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2) #Normal Distribution Fuction
    return prob_density
  


