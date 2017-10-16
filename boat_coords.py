#!/usr/bin/python

import gdb

class GetLevel(gdb.Function):
	"""Returns current level.
	Has no arguments.
	Needs to be called from main().
	Otherwise, returns random sheez.
	"""
	
	def __init__(self):
		super(GetLevel, self).__init__("get_level")
		
	def invoke(self):
		ptr = gdb.parse_and_eval('$rbp-0x50')
		level = deref_int_from_addr(ptr)
		return level
		
GetLevel()


class GetHash(gdb.Function):
	"""Returns the value of NotMd5Hash("XXXX"),
	where X represents a random char.
	Needs to be called after $rbp-0x140 has been
	written the hash, and before the call to memcmp.
	"""
	
	def __init__(self):
		super(GetHash, self).__init__("get_hash")
		
	def invoke(self):
		ptr = gdb.parse_and_eval('$rbp-0x140')
		magic = deref_string_from_addr(ptr)
		return magic
		
GetHash()


def load_coords(num):
	letters = ['A','B','C','D','E','F','G','H']
	numbers = ['1','2','3','4','5','6','7','8']
	coordinates = []
	
	for l in letters:
		for n in numbers:
			if (num & 1) > 0:
				coordinates.append(l+n)
			num = num >> 1
		
	return coordinates


def deref_long_from_addr(addr):
	p_long = gdb.lookup_type('long').pointer()
	val = gdb.Value(addr).cast(p_long).dereference()
	return val

	
def deref_int_from_addr(addr):
	p_int = gdb.lookup_type('int').pointer()
	val = gdb.Value(addr).cast(p_int).dereference()
	return val

	
def deref_string_from_addr(addr):
	p_str = gdb.lookup_type('char').pointer()
	val = gdb.Value(addr).cast(p_str).string()
	return val

	
def write_coords_to_file(filename):
	ptr = gdb.parse_and_eval('$rax')
	magic_num = deref_long_from_addr(ptr)
	coords = load_coords(magic_num)
	
	with open(filename, 'a') as f:
		for coord in coords:
			f.write(coord + '\n')

			
def write_level_to_file(filename, level):
	with open(filename, 'a') as f:
		f.write("^^LEVEL %d^^\n" % level)


def empty_file(filename):
	open(filename, 'a').close()
