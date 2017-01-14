#!/usr/bin/python

""" function returns next word in file @param file_obj - object of processed file """
def get_word(file_obj):
		for line in file_obj:
			for word in line.split():
				yield word