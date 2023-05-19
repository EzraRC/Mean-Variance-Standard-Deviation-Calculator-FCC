import numpy as np

def calculate(list):
    
    # Check if the list contains nine numbers
    if len(list) < 9:
        
        # ValueError to stop executing / print "List must contain nine numbers."
        raise ValueError("List must contain nine numbers.") 
    
    # Reshape the list into a 3x3 matrix
    matrix_3x3 = np.reshape(list, (3, 3))

    # Calculate means along different axes and overall mean
    means = [
        
        # Axis 1 - Columns
        np.mean(matrix_3x3, axis=0).tolist(),

        # Axis 2 - Rows
        np.mean(matrix_3x3, axis=1).tolist(),

        # Axis 3 - Flattened
        np.mean(np.array(list))
    ]

    # Calculate variances along different axes and overall variance
    variances = [
        
        # Axis 1 - Columns
        np.var(matrix_3x3, axis=0).tolist(),

        # Axis 2 - Rows
        np.var(matrix_3x3, axis=1).tolist(),

        # Axis 3 - Flattened
        np.var(np.array(list))
    ]

    # Calculate standard deviations along different axes and overall standard deviation
    standardDeviations = [
        
        # Axis 1 - Columns
        np.std(matrix_3x3, axis=0).tolist(),

        # Axis 2 - Rows
        np.std(matrix_3x3, axis=1).tolist(),

        # Axis 3 - Flattened
        np.std(np.array(list))
    ]

    # Find maximum values along different axes and overall maximum
    maxValues = [
        
        # Axis 1 - Columns
        np.max(matrix_3x3, axis=0).tolist(),

        # Axis 2 - Rows
        np.max(matrix_3x3, axis=1).tolist(),

        # Axis 3 - Flattened
        np.max(np.array(list))
    ]

    # Find minimum values along different axes and overall minimum
    minValues = [
        
        # Axis 1 - Columns
        np.min(matrix_3x3, axis=0).tolist(),

        # Axis 2 - Rows
        np.min(matrix_3x3, axis=1).tolist(),

        # Axis 3 - Flattened
        np.min(np.array(list))
    ]
    
    # Calculate sums along different axes and overall sum
    sums = [
        
        # Axis 1 - Columns
        np.sum(matrix_3x3, axis=0).tolist(),

        # Axis 2 - Rows
        np.sum(matrix_3x3, axis=1).tolist(),

        # Axis 3 - Flattened
        np.sum(np.array(list))
    ]
    
    # Store all the calculations in proper format dictionary
    calculations = {
        
        # Means
        "mean": means,
        
        # Variance
        "variance": variances,
        
        # Standard Deviation
        "standard deviation": standardDeviations,
        
        # Maximum Values
        "max": maxValues,
        
        # Minimum Values
        "min": minValues,
        
        # Sums
        "sum": sums
    }

    return calculations
