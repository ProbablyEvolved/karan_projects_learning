# Find Cost of Tile to Cover W x H Floor
# Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.
# https://github.com/karan/Projects
# 006

print('Enter the Cost Per Square Meter of the Tile(in Rupees): ', end='')
rate = float(input())

print('Enter the Width of the Room(in Meters): ', end='')
width = float(input())

print('Enter the Length of the Room(in Meters): ', end='')
length = float(input())

total_cost = width * length * rate

print(f'Total Cost of Tiles for the Given Room = {total_cost:.2f}')