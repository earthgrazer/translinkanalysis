import argparse
import xml.etree.ElementTree as ET

def find_centre_of_circle(coordinates):
	if coordinates == None:
		return
	
	west_most_coord = None
	east_most_coord = None
	north_most_coord = None
	south_most_coord = None
	
	coordinates = coordinates.split(' ')
	
	if len(coordinates) == 0:
		return
	
	for coordinate_tuple in coordinates:
		coordinate_tuple = coordinate_tuple.split(',')
		if len(coordinate_tuple) < 2:
			continue
		lon = float(coordinate_tuple[0])
		lat = float(coordinate_tuple[1])
		if lon < west_most_coord or west_most_coord == None:
			west_most_coord = lon
		if lon > east_most_coord or east_most_coord == None:
			east_most_coord = lon
		if lat > north_most_coord or north_most_coord == None:
			north_most_coord = lat
		if lat < south_most_coord or south_most_coord == None:
			south_most_coord = lat
	
	print(str((west_most_coord + east_most_coord) / 2) + ',' + str((north_most_coord + south_most_coord) / 2))
		

parser = argparse.ArgumentParser(description='Extract the centres of radii from KML')
parser.add_argument('--input', '-i', dest='input', required=True, metavar='INPUT_FILE', help='input KML file path')

args = parser.parse_args()

ns = {'kml': 'http://www.opengis.net/kml/2.2'}

tree = ET.parse(args.input)
root = tree.getroot()
coordinates_list = root.findall('kml:Document/kml:Placemark/kml:Polygon/kml:outerBoundaryIs/kml:LinearRing/kml:coordinates', ns)

for coordinates in coordinates_list:
	find_centre_of_circle(coordinates.text)