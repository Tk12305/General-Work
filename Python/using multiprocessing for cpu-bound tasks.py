from multiprocessing import Pool

def square(n):
    return n * n

with Pool(4) as p:
    result = p.map(square, [1, 2, 3, 4, 5])
    print(result) # [1, 4, 9, 16, 24]