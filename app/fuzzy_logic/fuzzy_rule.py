#!/usr/bin/python

import fuzzy_set

class FuzzyRule:
	# if x1_set contains first input value
	x1_set = None
	# and x2_set contains second input value
	x2_set = None
	# then output belongs to y_set
	y_set = None
	
	def __init__(self, x1_set_val, x2_set_val, y_set_val):
		self.x1_set = x1_set_val
		self.x2_set = x2_set_val
		self.y_set = y_set_val
		
		self.x1_set.add_rule(self)
		x2_set_val.add_rule(self)
		y_set_val.add_rule(self)