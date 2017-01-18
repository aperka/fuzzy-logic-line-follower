#!/usr/bin/python

import fuzzy_rule

class FuzzifiedVal:
	member_val = 0
	fuzzy_set = None
	
	def __init__(self, member_val_val, fuzzy_set_val):
		self.member_val = member_val_val
		self.fuzzy_set = fuzzy_set_val