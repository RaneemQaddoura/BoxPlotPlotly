""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                                                                        """
"""                              Box Plot                                  """
"""                Plot a box plot from a data file using plotly           """
"""                             @author: Raneem                            """
"""   @email: rqaddoura@philadelphia.edu.jo, raneem.qaddoura@gmail.com     """
"""                                 v1.0                                   """
"""                                                                        """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Box Plot Plotly
# Plot a box plot from a data file using plotly
# The CSV file is of a single data set for the statistical analysis of each run against several algorithms
# columns represent the run number
# Rows represent the algorithm
    

import plotly.graph_objs as go
import plotly.io as pio

import numpy as np
import os

def readDataset(directory, filename):
    """
    Reads the dataset file and store a list of Point ............

    Parameters
    ----------
    directory : str
        The file location of the dataset
    filename : str
        The dataset file name

    Returns
    -------
    ndarray
        The data as a numpy matrix
    """
    global nPoints, nValues, k, points, labelsTrue
    rawData = open(os.path.join(directory + filename), 'rt')  
    data = np.loadtxt(rawData, delimiter=",")
    return data




directory = ""
alg = ["Alg1","Alg2","Alg3","Alg4","Alg5","Alg6","Alg7"]
dataset_List = ['DS1']
left = 50
right = 50
bottom = 50
top = 30
for j in range(len(dataset_List)):

    data = []
    #rows represent the algorithm
    #columns represent the run number
    filename = dataset_List[j] + ".csv"
    dataFile = readDataset(directory, filename)
    
    for z in range(len(dataFile)):
        data.append(go.Box(      
            y=dataFile[z],
            name = alg[z]
        ))
            
    layout = go.Layout(
        legend=dict(font=dict(size=18)),
        font=dict(size=22),
        yaxis = dict(range=[0,1],showline=True),
        showlegend=True,
        margin=go.layout.Margin(
                l= left,
                r=right,
                b=bottom,
                t=top,
                pad=0
       )
    )
    
    fig = go.Figure(data=data, layout=layout)
    pio.write_image(fig, directory + str(dataset_List[j]) + ".pdf")