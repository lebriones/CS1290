def min_squares(n):

    squares =[]
    i = 1
    while i*i <= n:
        squares.append(i*i)
        i+=1
    
    