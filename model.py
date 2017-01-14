#!/usr/bin/python

import fuzzy_set
import fuzzy_rule
import fuzzified_val
import file

class Model:
	x1_linguistic_val = []
	x2_linguistic_val = []
	y_linguistic_val = []
	
	def __init__(self):
		conf_file = open("init.conf", "r")
		
		generator = file.get_word(conf_file)
		
		for word in generator:
			if (word == 'x1'):
				break
		
		self.get_sets_from_file("x2", generator, self.x1_linguistic_val)
		self.get_sets_from_file("y", generator, self.x2_linguistic_val) 
		self.get_sets_from_file("rules", generator, self.y_linguistic_val)
		self.get_rules_from_file(generator)
		
		conf_file.close()
	
	""" function initializes list of fuzzy sets with data from file, @param end_mark - character indicated the end of data,
	@param generator - generator of words from file with data, @param linguistic_val - list to which new fuzzy sets are written"""
	def get_sets_from_file(self, end_mark, generator, linguistic_val):
		for word in generator:
			if (word == end_mark):
				break
			else:
				set = fuzzy_set.FuzzySet(word, int(next(generator)), int(next(generator)))
				linguistic_val.append(set)
	
	""" function initializes list of fuzzy rules with data from file, @param generator - generator of words from file with data"""
	def get_rules_from_file(self, generator):
		for word in generator:
			x1_set_val = self.find_set(word, self.x1_linguistic_val)
			# 'and'
			next(generator)
			x2_set_val = self.find_set(next(generator), self.x2_linguistic_val)
			# 'then'
			next(generator)
			y_set_val = self.find_set(next(generator), self.y_linguistic_val)
			
			rule = fuzzy_rule.FuzzyRule(x1_set_val, x2_set_val, y_set_val)
	
	""" function finds set with given name, @param name - name of set, @param linguistic_val - list in which set is sought """
	def find_set(self, name, linguistic_val):
		for set in linguistic_val:
			if set.name == name:
				return set
	
	""" function fuzzifies given value @param val - fuzzified value, @param linguistic_val - value's linguistic variable"""
	def fuzzify(self, val, linguistic_val):
		fuzzified_vals = []
		
		for set in linguistic_val:
			member_val_val = set.get_truth_value(val)
			
			if member_val_val != 0.0:
				fuzzified_val_val = fuzzified_val.FuzzifiedVal(member_val_val, set)
				fuzzified_vals.append(fuzzified_val_val)
				
		return fuzzified_vals
	
	""" function returns fuzzified value of output based on fuzzy rules set @param fuzzified_vals_x1 - fuzzified values of first input,
	@param fuzzified_vals_x2 - fuzzified values of second input"""
	def conclude(self, fuzzified_vals_x1, fuzzified_vals_x2):
		fuzzified_vals_y = []
		
		for fuzz_x1 in fuzzified_vals_x1:
			for fuzz_rule in fuzz_x1.fuzzy_set.rules_list:
				fuzz_x2 = self.find_fuzzified_val(fuzz_rule.x2_set, fuzzified_vals_x2)
				
				if fuzz_x2 != None:
					member_val_y = min(fuzz_x1.member_val, fuzz_x2.member_val)
					fuzz_y = fuzzified_val.FuzzifiedVal(member_val_y, fuzz_rule.y_set)
					fuzzified_vals_y.append(fuzz_y)
					
		return fuzzified_vals_y
	
	""" finds in the given list of fuzzified values specified set @param searched_set - searched set, @param fuzzified_vals - list of fuzzified values"""
	def find_fuzzified_val(self, searched_set, fuzzified_vals):
		for fuzz_val in fuzzified_vals:
			if fuzz_val.fuzzy_set is searched_set:
				return fuzz_val
				
		return None
		
	# defuzzify with heights method
	""" function defuzzifies given fuzzified value @param fuzzified_vals - defuzzified value """
	def defuzzify(self, fuzzified_vals):
		divider = 0.0
		divident = 0.0
	
		for fuzz_val in fuzzified_vals:
			divider += fuzz_val.member_val
			divident += (fuzz_val.member_val * fuzz_val.fuzzy_set.get_medium())
			
		if divider != 0.0:
			return divident / divider
		else:
			return 0.0
	
	# x1 - sensor on the left, x2 - sensor on the right
	""" function returns value of angle for given sensors' values @param x1 - first sensor's output, @param x2 - second sensor's output """
	def get_angle(self, x1, x2):
		fuzzified_x1 = self.fuzzify(x1, self.x1_linguistic_val)
		fuzzified_x2 = self.fuzzify(x2, self.x2_linguistic_val)
		
		fuzzified_y = self.conclude(fuzzified_x1, fuzzified_x2)
		
		y = self.defuzzify(fuzzified_y)
		
		return y
