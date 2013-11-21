#!/usr/bin/python
import sys, os, glob, shutil, numpy, math

from pylab import *

import matplotlib
import matplotlib.pyplot as plt

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-N", "--max_pts", dest="max_pts", help="Target number of points in grid", metavar="NUM")
parser.add_option("-n", "--start_pts", dest="start_pts", help="Number of starting points for the bisection series", metavar="NUM")
parser.add_option("-d", "--divs", dest="num_divs", help="Number of bisections to print in the series.", metavar="DIVS")

options, args = parser.parse_args()

if not options.max_pts:
	run_mode = 2
else:
	run_mode = 1

if run_mode == 2:
	if not options.start_pts:
		parser.error("Either max_pts or start_pts and divs are required.")
	else:
		if not options.num_divs:
			parser.error("Divs are required when max_pts is not provided.")

if run_mode == 1:
	target = float(options.max_pts)
	cur_pts = target
	last_pts = target
	bisections = 0
	while cur_pts >= 10:
		bisections = bisections + 1
		last_pts = cur_pts
		cur_pts = (cur_pts + 6.0) / 4.0

	bisections = bisections-1
	cur_pts = int(last_pts)
	print "Bisections: ", bisections
	print "Smallest point set: ", int(cur_pts)

	print "Bisection series is:"
	i = 0
	while i < bisections:
		i = i+1
		cur_pts = cur_pts * 4.0 - 6.0
		print "    ", int(cur_pts)
else:
	bisections = int(options.num_divs)
	cur_pts = float(options.start_pts)
	print "Bisections: ", bisections
	print "Smallest point set: ", int(cur_pts)

	print "Bisection series is:"
	i = 0
	while i < bisections:
		i = i+1
		cur_pts = cur_pts * 4.0 - 6.0
		print "    ", int(cur_pts)
	



