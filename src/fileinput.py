def get_file(filename):
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        return [[float(val) for val in line.split()] for line in lines[:]]
    except IOError:
        print(filename+" is missing.")
        
