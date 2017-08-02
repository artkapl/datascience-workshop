# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 15:47:19 2017
"""
# climate change project

#files required:
    
# 1)data.csv => contains 
#    -station ID => Index[0]
#    -temperature => Index[3]

# 2)site_detail.csv => contains:
#    -station ID => Index[0]
#    -Latitude => Index[2]
#    -Longitude => Index[3]
#    -Country => Index[9]

# open both files, skip forward until header
# skip header

# read data.csv => dict {station ID: [temperature]}
# read site_detail =>dict {station ID: [lat, long, country]

# merge files {station ID, [temp, lat, long, country]

import csv
from pprint import pprint
from collections import Counter, defaultdict
from math import trunc

debug = False

def make_station_ID_dict(infile='../../weather_data/site_detail.csv'):
    '''
    read data from infile, create station_ID_dict {station_ID: [lat, lon, country]}
    infile = filename
    returns station_ID_dict
    '''
    station_ID_dict = defaultdict(list)

    with open(infile) as sitefile:
        site_detail_reader = csv.reader(sitefile, delimiter=';', quotechar='"')
        
        for station_ID, _t1, lat, lon, _t2, _t3, _t3, _t4, country, *_rest in site_detail_reader:

            if '%' in station_ID:
                continue #skip header
            station_ID_dict[station_ID].extend([float(lat), float(lon), country.rstrip()])
        if debug:
            pprint(station_ID_dict)
            
        return station_ID_dict


def make_measurement_freq_file(station_ID_dict, outfile='../../weather_data/station measurement frequency.csv', datafile='../../weather_data/data.csv'):    
    """
    counts nr of measurements and temperature from infile and writes it in outfile
    input station_ID_dict, outfile, datafile
    returns dict {station_ID: {year: [measurements]}}
    """
    temp_measurements = defaultdict(lambda : defaultdict(list))

    outfile = open(outfile, "w", newline='')
         
    with open(datafile) as datafile:
        data_reader = csv.reader(datafile, delimiter=';', quotechar='"')
        data_writer = csv.writer(outfile, delimiter=',', quotechar='"')  
        data_writer.writerow(['station_ID', 'num of measurements 1961-2000', 'lat', 'lon'])
            
        temp_counter = Counter()
        
        for station_ID, _t1, year, temperature, *_rest in data_reader:
            if '%' in station_ID:
                continue   # skip header     
            
            temp_counter[station_ID]  += 1 # maybe unecessary
            temp_measurements[int(station_ID)][trunc(float(year))].append(float(temperature))
            
   # write station ID and number of measurements in csv file     
    
        for sid, l in station_ID_dict.items():
            count = temp_counter[sid]
            data_writer.writerow([sid, count, station_ID_dict[sid][0],  station_ID_dict[sid][1] ])
        if debug:
            pprint(temp_measurements)

    outfile.close()
        
    return temp_measurements
        
def calc_avg(measurements_dict):
    """
    sum up temperature values per station per year and calculates temp average
    returns {station_ID: {year: average}}
    """
    temp_averages = dict()
    for station in measurements_dict.keys():
        
        for year in measurements_dict[station].keys():
            L = measurements_dict[station][year]
            if len(L) != 0:
                average = sum(L)/len(L)
            else:
                average = float('NaN')
            # temp_averages = {station_ID: {year: average}}
            if station not in temp_averages:
                temp_averages[station] = {year: None}
            elif year not in temp_averages[station]:
                temp_averages[station].update({year: None})
            temp_averages[station][year] = average
    if debug:
        pprint(temp_averages)
    return temp_averages
    
    
def write_station_year_avg_file(measurements_dict, outfile='../../weather_data/station_year_avg.csv'):
    """
    writes csv output file containing the yearly average temperature measurement / station
    return None
    """

    with open(outfile, "w", newline='') as f:
        data_writer = csv.writer(f, delimiter=',', quotechar='"')
        data_writer.writerow(['station_ID', 'year', 'average temperature'])

        for station_ID, _v in measurements_dict.items():
            for year, average in _v.items():
                data_writer.writerow([station_ID, year, average])

def time_sort(year_dict, start_year=1980, end_year=2001):
    """
    input is dict with years in which measurements were taken as values {station_ID: {years}}
    returns dict {station_ID: bool} True if subset
    """
    time_dict = dict()
    for station_ID in year_dict.keys():
        time_dict[station_ID] = year_dict[station_ID].issubset(range(start_year, end_year))
    return time_dict
                
def calc_worldwide_avg_temp_per_year(measurements_dict, filtered_list):
    """
    input: {station_ID: {year: [measurements]}}, list from year_filter()
    calculates worldwide average yearly temperature over all stations
    returns {year: worldwide temperature average}
    """
    _t = defaultdict(list)
    avg_temp_dict = dict()
    
    for station_ID, _v in measurements_dict.items():
        if station_ID in filtered_list:
            for year, measurements in _v.items():
                _t[year].extend(measurements)
            
    for year, measurements in _t.items():
        average = sum(measurements)/len(measurements)
        avg_temp_dict[year] = average
    pprint(avg_temp_dict)    
    return avg_temp_dict
        
                
    

def write_worldwide_avg_temp_per_year(filtered_station_IDs):
    """
    writes csv output file containing the worldwide yearly average temperature measurement 
    return None
    """
    pass
    

def calc_years_of_measurements(measurements_dict):
    '''
    input: {station_ID: {year: [measurements]}}
    calculates measurement years per station ID
    returns dict {station_ID: set(years which have measurements)}
    '''
    
    year_dict = dict()
    
    
    for station_ID, _v in measurements_dict.items():
        s = set()
        year_dict[station_ID] = s
        for year, measurements in _v.items():
            if measurements: # if measurements not empty
                year_dict[station_ID] |= {year}
        
    return year_dict

def year_filter(year_measurement_dict):
    return [station for station in year_measurement_dict.keys() if year_measurement_dict[station]]
    
                
if __name__ == '__main__':
    station_ID_dict = make_station_ID_dict()
    temp_measurements = make_measurement_freq_file(station_ID_dict)
    temp_avg = calc_avg(temp_measurements)
    write_station_year_avg_file(temp_avg)
    _sorted_stations = time_sort(calc_years_of_measurements(temp_measurements))  
    _yf = (year_filter(_sorted_stations))
    calc_worldwide_avg_temp_per_year(temp_measurements, _yf)


    
    
    