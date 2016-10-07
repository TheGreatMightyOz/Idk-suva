def get_file(filename):
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        cols, rows = cols, rows = (int(val) for val in lines[0].split())
        return [[int(val) for val in line.split()] for line in lines[1:]]
    except IOError:
        print(filename+" is missing.")
        
