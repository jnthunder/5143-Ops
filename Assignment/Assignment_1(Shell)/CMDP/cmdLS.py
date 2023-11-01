import os
from os import listdir
import stat
from pwd import getpwuid
from grp import getgrgid
import datetime
import math

def ls(**kwargs):

	S = ""
	i = int
	flags = kwargs.get('flags')							
	print("\n")

	for s in flags:										# Files pulled from the list and placed in a string
		S += s

	files = os.listdir()								# Current directory

	if S == '':											# If there are no flags the Crrent directory file names are printed out
		files = [f for f in files if f[0] != '.']
		files.sort()
		print("\n", *files)
	else:
		if 'l' in S:									# If l is in flags, longlisting definition below is pulled and remaining flags 
			longListing(files, S)						# 		are used in the longlisting function
		elif 'a' in S:									# If a is is in flags, it will allow the hidden fill names to be shown
			files.sort()
			print("\n", *files)
		elif 'h' in S:									# h is just set up to show the same as a if it is not utilized properly with
			files = [f for f in files if f[0] != '.']	#		the longlisting function(or the l flag is forgotten)
			files.sort()
			print("\n", *files)	
		
def longListing(files, flags):									# this definition is set up for long listing and it's flags

	print("\n")
	Files = ""

	if 'a' in flags:											# If flag a was utilized with ls -l it will allow hidden files to be shown
		Files = files
	else:		
		Files = [f for f in files if f[0] != '.']				# If flag a is not utilized with ls -l, hidden files will stay hidden

	for n in Files:												
		entry = []
		filestats = os.lstat(os.path.abspath(os.path.join(os.getcwd(), n)))
		
		#permissions
		modes = ['r','w','x']
		mode = ''

		#Establishing the filetype
		if stat.S_ISDIR(filestats.st_mode):
			filetype = 'd'
			entry.append(filetype)
		elif stat.S_ISLNK(filestats.st_mode):
			filetype = 'l'
			entry.append(filetype)
		else:
			filetype = '-'
			entry.append(filetype)
			
		#binary representation for permissions
		#evaluate last 9 bits
		st_perms = bin(filestats.st_mode)[-9:]
		for i, perm in enumerate(st_perms):
			if perm == '0':
				mode += '-'                              
			else:
				mode += modes[i % 3]    
		entry.append(mode)

		mode += " " + str(filestats.st_nlink) + " " 
		entry.append(str(filestats.st_nlink))

		mode += getpwuid(filestats.st_uid).pw_name + " "
		entry.append(getpwuid(filestats.st_uid).pw_name)
		mode += getgrgid(filestats.st_gid).gr_name + " "
		entry.append(getgrgid(filestats.st_gid).gr_name)
		mode += str(filestats.st_size) + " "
		
		#returns human readable or bytes
		if 'h' in flags:											# If h is in the flags after ls -l the code changes the file size
			entry.append(convert_size(filestats.st_size).rjust(9))	#		from bits to bytes or Human Readable
		else:
			entry.append(str(filestats.st_size).rjust(7))			# If h is not in the flags the file size stays in bits
			
		mode += str(datetime.datetime.fromtimestamp(filestats.st_mtime).strftime('%b %d %H:%M')) + " "
		entry.append(str(datetime.datetime.fromtimestamp(filestats.st_mtime).strftime('%b %d %H:%M')))
		
		print(*entry, n)
	return
		
def convert_size(size_bytes): 
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])
