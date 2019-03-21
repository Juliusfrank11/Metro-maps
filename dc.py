# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 12:37:08 2019

@author: PC
"""

import networkx as nx
import os

def add_edges(metro = nx.Graph(),line = []):
    for i in line:
        if line.index(i) < (len(line) - 1):
            metro.add_edge(line[line.index(i)], line[line.index(i)+1])

metro = nx.Graph()
red_line = ["Shady Grove", "Rockville", "Twinbrook", "Grosvenor–Strathmore", "Medical Center", "Bethesda", "Friendship Heights", "Tenleytown–AU", "Van Ness–UDC", "Cleveland Park", "Woodley Park", "Dupont Circle", "Farragut North", "Metro Center", "Gallery Place", "Judiciary Square", "Union Station", "NoMa–Gallaudet U", "Rhode Island Avenue–Brentwood", "Brookland–CUA", "Fort Totten", "Takoma", "Silver Spring", "Forest Glen", "Wheaton", "Glenmont"]
add_edges(metro,red_line)
blue_line = ["Franconia–Springfield", "Van Dorn Street", "King Street – Old Town", "Braddock Road", "Ronald Reagan Washington National Airport" , "Crystal City" , "Pentagon City" , "Pentagon" , "Arlington Cemetery" , "Rosslyn" , "Foggy Bottom – GWU" , "Farragut West" , "McPherson Square" , "Metro Center" , "Federal Triangle" , "Smithsonian" , "L'Enfant Plaza" , "Federal Center SW" , "Capitol South" , "Eastern Market" , "Potomac Avenue" , "Stadium–Armory" , "Benning Road" , "Capitol Heights" , "Addison Road" , "Morgan Boulevard" , "Largo Town Center"]
add_edges(metro,blue_line)
orange_line = ["Franconia–Springfield" , "Van Dorn Street" , "King Street – Old Town" , "Braddock Road" , "Ronald Reagan Washington National Airport" , "Crystal City" , "Pentagon City" , "Pentagon" , "Arlington Cemetery" , "Rosslyn" , "Foggy Bottom – GWU" , "Farragut West" , "McPherson Square" , "Metro Center" , "Federal Triangle" , "Smithsonian" , "L'Enfant Plaza" , "Federal Center SW" , "Capitol South" , "Eastern Market" , "Potomac Avenue" , "Stadium–Armory" , "Benning Road" , "Capitol Heights" , "Addison Road" , "Morgan Boulevard" , "Largo Town Center"]
add_edges(metro,orange_line)
yellow_line = ["Huntington" , "Eisenhower Avenue" , "King Street – Old Town" , "Braddock Road" , "Ronald Reagan Washington National Airport" , "Crystal City" , "Pentagon City" , "Pentagon" , "L'Enfant Plaza" , "Archives" , "Gallery Place" , "Mount Vernon Square" , "Shaw – Howard University" , "U Street" , "Columbia Heights" , "Georgia Avenue–Petworth" , "Fort Totten"]
add_edges(metro,yellow_line)
green_line = ["Branch Avenue" , "Suitland" , "Naylor Road" , "Southern Avenue" , "Congress Heights" , "Anacostia" , "Navy Yard–Ballpark" , "Waterfront" , "L'Enfant Plaza" , "Archives" , "Gallery Place" , "Mount Vernon Square" , "Shaw – Howard University" , "U Street" , "Columbia Heights" , "Georgia Avenue–Petworth" , "Fort Totten" , "West Hyattsville" , "Prince George's Plaza" , "College Park–University of Maryland" , "Greenbelt"]
add_edges(metro,green_line)
silver_line = ["Wiehle–Reston East" , "Spring Hill" , "Greensboro" , "Tysons Corner" , "McLean" , "East Falls Church" , "Ballston–MU" , "Virginia Square–GMU" , "Clarendon" , "Court House" , "Rosslyn" , "Foggy Bottom – GWU" , "Farragut West" , "McPherson Square" , "Metro Center" , "Federal Triangle" , "Smithsonian" , "L'Enfant Plaza" , "Federal Center SW" , "Capitol South" , "Eastern Market" , "Potomac Avenue" , "Stadium–Armory" , "Benning Road" , "Capitol Heights" , "Addison Road" , "Morgan Boulevard" , "Largo Town Center"]
add_edges(metro,silver_line)
#nx.draw(metro_distance, with_labels = True, node_size = 100)
nx.write_graphml(metro, os.getcwd() + "\\test.graphml")
print("clossness centality")
print(nx.closeness_centrality(metro))
print("degree centality")
print(nx.degree_centrality(metro))
print("betweenness centrality")
print(nx.betweenness_centrality(metro))
print("circuit rank")
print(nx.number_of_edges(metro)-nx.number_of_nodes(metro)+1)
print("Average clustering")
print(nx.average_clustering(metro))
