#!/usr/bin/python

import xml.etree.ElementTree as xml
import random
shows = [(1, 'Mutts and Mongrels', 'June 10, 2045', 'Snootshirem FancyPlace')];
breeds = [
    (1, 'Husky', 'images/google.png', '9:00am'),
    (2, 'Collie', 'images/amazon.png', '10:00am'),
    (3, 'Irish Wolfhound', 'images/youtube.png', '11:00am')
]
dogs = [
    (1, 1, 'Floofie', 'Mark Steyn'),
    (2, 1, 'Snoofie', 'Rush Lim'),
    (3, 1, 'Doofie', 'Sean Hanitty'),
    (4, 2, 'Arfie', 'Dianne Rheme'), 
    (5, 2, 'Scarfie', 'Terri Gross'),
    (6, 2, 'Barfie', 'Ira Gross'),
    (7, 3, 'C-Sharp', 'Ludwig Beethoven'),
    (8, 3, 'D-minor', 'Amadeu Mozart'),
    (9, 3, 'G-minor', 'Engelbert Humperdink')
]

model = xml.Element('mxGraphModel')
root = xml.Element('root')
model.append(root)
zero = xml.Element('mxCell', id='0')
one = xml.Element('mxCell', id='1', parent='0')