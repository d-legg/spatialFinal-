# import libraries here
import pandas as pd
import geopandas as gpd
import math as math
import matplotlib.pyplot as plt

# these shapefiles will be used for testing
counties = gpd.read_file('oregonCounties/tl_rd22_41_cousub.shp')
roads = gpd.read_file('oregonRoads/tl_rd22_41_arealm.shp')

def main(file):
    while True:
        # after every command (end, view, etc), the console will return to this message. this will be like our menu dashboard of different commands the user can do.
        print('\nWelcome to the vibe, here is some options:\n\tend - end program\n\tview - return basic info of file\n\tread - print the file table\n\treadHead - print specified rows\n\treproject - change crs\n')

        # command is set to be empty, and will turn into whatever the user types in the terminal. if you type view after the initial message, command = 'view'
        command = input('')

        # user types 'end' -> kill the program
        if command == 'end':
            print('thanks for contributing to Big Maps!')
            break

        # user types 'view' -> display info of shape file
        if command == 'view':
            print(f"--file info ('back' to return to menu):\n\trows: %i\n\tcols: %i" % (file.shape[0], file.shape[1]))
            print(f"\tcoordinate system: %s" % (file.crs))

            while True:
                viewCommand = input('')
                if viewCommand == 'back':
                    break

        # user types 'read' -> display the shapefile table (try print(file) or something along those lines, display the whole thing)
        if command == 'read':
            pass # delete this pass line when you create the print statement code

        # user types 'readHead' -> ask for number of rows, print with .head() function
        if command == 'readHead':
            while True:
                # headCount will be a number that's typed as a string in input, converted to a integer in headCountINT. use headCountINT as the actual number to place in the head. 
                headCount = input('How many rows? :')
                headCountINT = int(headCount)

                # right here print the file.head() using the number given from headCountINT
                # ALSO -> include the a break statement on the line after the print() statement, to make sure the loop breaks. check line 22 or line 32 for an example.

        # user types in 'reproject' -> allow to change crs of the file.
        if command == 'reproject':
            while True:
                print('Current CRS: %s' % (file.crs))

                # newCRS will ideally already be formatted correctly as a string. we are expecting the input of newCRS to be along the lines of 'ESPG:32610', 'ESPG:31020', etc. For testing, find any ESPG and input that when prompted.
                newCRS = input('\nNew CRS:')

                # use the .to_crs() function to reproject the file. Remember the break statement right after printing or the program will be stuck in a loop!!

        

# this is where everything is actually run, replace counties with any file you want to run the same program with a different shapefile. 
main(counties)