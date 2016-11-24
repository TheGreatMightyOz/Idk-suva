def get_file(filename):
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        cols, rows = (int(val) for val in lines[0].split())
        return [[int(val) for val in line.split()] for line in lines[:]]
    except IOError:
        print(filename+" is missing.")
        
