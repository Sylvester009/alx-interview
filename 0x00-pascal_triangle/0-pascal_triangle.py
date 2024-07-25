# function for pascal triangle
def pascal_triangle(n):
    # check if n is lesser than 0
    if n <= 0:
        return []
    
    # initialize triangle by creating the first row
    triangle = [[1]]
    
    # iterate through all the row
    for i in range(1, n):
        # initialize start for
        # every first digit in a row
        start = [1]
        
        # fill up the middle of the row
        for j in range(1, i):
            start.append(triangle[i-1][j-1] + triangle[i-1][j])
        start.append(1)
            
        # add the row to the triangle
        # and return it
        triangle.append(start)
    return triangle