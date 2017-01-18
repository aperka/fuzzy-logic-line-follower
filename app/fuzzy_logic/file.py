#!/usr/bin/python

def get_word(file_obj):
		for line in file_obj:
			for word in line.split():
				yield word