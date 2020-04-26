# CHALLENGE PROBLEMS
# YOU MAY NOT USE ANY ADDITIONAL LIBRARIES OR PACKAGES TO COMPLETE THIS CHALLENGE

# Divvy is Chicago's bike share system, which consists of almost 600 stations scattered
# around the city with blue bikes available for anyone to rent. Users begin a ride by removing
# a bike from a dock, and then they can end their ride by returning the bike to a dock at any Divvy 
# station in the city. You are going to use real data from Divvy collected at 1:30pm on 4/7/2020 
# to analyze supply and demand for bikes in the system. 

# NOTE ** if you aren't able to run this, type "pip install json" into your command line
import json

# do not delete; this is the data you'll be working with
divvy_stations = json.loads(open('divvy_stations.txt').read())

# PROBLEM 1
# find average number of empty docks (num_docks_available) and 
# available bikes (num_bikes_available) at all stations in the system

# First we find num_docks-available and store in a new list named empty_docks
empty_docks = [station['num_docks_available'] for station in divvy_stations]
# Then we find num_docks-available and store in a new list named empty_docks
bikes_available = [station['num_bikes_available'] for station in divvy_stations]

# Then we find out the average number of empty docks
avg_empty_docks = sum(empty_docks)/len(divvy_stations)
average_bikes = sum(bikes_available)/len(divvy_stations)

# PROBLEM 2
# find ratio of bikes that are currently rented to total bikes in the system (ignore ebikes)
# Here we assume that the num_docks_availble indicates the number of rented bikes and 
# num_bikes_available indicates the bikes that are available for rent
sum(empty_docks)/(sum(empty_docks)+sum(bikes_available))


# PROBLEM 3 
# Add a new variable for each divvy station's entry, "percent_bikes_remaining", that shows 
# the percentage of bikes available at each individual station (again ignore ebikes). 
# This variable should be formatted as a percentage rounded to 2 decimal places, e.g. 66.67%

for station in divvy_stations:
    percentage = station['num_bikes_available']/(station['num_bikes_available']+station['num_docks_available'])
    percentage = "{0:.2%}".format(percentage)
    station.update({'percent_bikes_remaining':percentage})


