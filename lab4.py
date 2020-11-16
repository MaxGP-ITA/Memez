import math
import urllib

def seq_sqrt(xs):
    sqrts = []  
    for i in range(len(xs)):
        sqrts.append(math.sqrt(xs[i]))    
    return sqrts

def mean(xs):
    avg = 0.00
    for i in range(len(xs)):
        avg = avg + float(xs[i])
    avg = avg / len(xs)
    return avg

def noaa_string():
    url = "http://tgftp.nws.noaa.gov/data/observations/metar/decoded/EGHI.TXT"
    noaa_data_string = urllib.request.urlopen(url).read()
    return noaa_data_string.decode("utf-8")

def noaa_temperature(s):
    noaalist = ""
    noaalist = s.split(' ')
    return noaalist[32].replace('(', '')

def wc(filename):
    f = open(r"C:/Users/maxgi/Documents/Python Labs/" + filename, 'r')
    return len(f.read().split(' '))
    f.close()
    
def line_averages(filename):
    output = []
    f = open(r"C:/Users/maxgi/Documents/Python Labs/" + filename, 'r')        
    for lines in f.readlines():
        output.append(mean(lines.split(',')))

    return output   
    f.close()

def count_sub_in_file(filename,s):
    file = ""
    counter = 0
    f = open(r"C:/Users/maxgi/Documents/Python Labs/" + filename, 'r')
    file = f.read()
    return len(file.split(s)) - 1
    f.close()