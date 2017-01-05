#!/usr/bin/python

import fuzzy_rule

class FuzzySet:
	name = ""

	# fuzzy set range
	low = 0
	high = 0
	
	# list with all fuzzy rules associated with this set
	rules_list = []
	
	def __init__(self, name_val, low_val, high_val):
		self.name = name_val
		self.low = low_val
		self.high = high_val
		
		self.rules_list = []
		
	# fuzzy function shape - triangle
	def get_truth_value(self, val):
		medium = (self.low + self.high) / 2
		
		result = 0.0
		
		if (val >= self.low) and (val <= medium):
			result = 2 * (val - self.low) / (self.high - self.low)
			
		if (val <= self.high) and (val > medium):
			result = 2 * (self.high - val) / (self.high - self.low)
			
		return result
		
	def add_rule(self, fuzzy_rule_val):
		self.rules_list.append(fuzzy_rule_val)
		
	def get_medium(self):
		result = (self.low + self.high) / 2
		return result