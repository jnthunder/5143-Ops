import os
from os import listdir
import stat
from pwd import getpwuid
from grp import getgrgid
import datetime
import math

def ls(**kwargs):
	S = ""
	F = ""
	#directory = kwargs.get('params')
	flags = kwargs.get('flags')
	for s in flags:
		S += s
		# print(S[0])
		# print(S[1])
		# print(S[2])
	# for s in S:
	# 	F += s
	# 	print(F[0])
	files = os.listdir()
	#if flags:
	if S == '':
		files = [f for f in files if f[0] != '.']
		files.sort()
		print("\n", *files)
	elif 'l' in S[0]:
		longListing(files, S)
	elif 'a' in S[0]:
		files.sort()
		print("\n", *files)
	elif 'h' in S[0]:
		files = [f for f in files if f[0] != '.']
		files.sort()
		print("\n", *files)	
	# else:
    #      files = [f for f in files if f[0] != '.']
    #      files.sort()
    #      print("\n", *files)
	#return
		
def longListing(files, S):
	print("\n")
    #print(os.getcwd())
	#print(*files)
	if 'l' in S[0]:
		for n in files:
			
			if 'a' in S:
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
				if 'h' in S:
					entry.append(convert_size(filestats.st_size).rjust(9))
				else:
					entry.append(str(filestats.st_size).rjust(7))
					
				mode += str(datetime.datetime.fromtimestamp(filestats.st_mtime).strftime('%b %d %H:%M')) + " "
				entry.append(str(datetime.datetime.fromtimestamp(filestats.st_mtime).strftime('%b %d %H:%M')))
				
				print(*entry, n)
				
			else:
				#default behavior should not show hidden                  
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
				if 'h' in S:
					entry.append(convert_size(filestats.st_size).rjust(9))
				else:
					entry.append(str(filestats.st_size).rjust(7))
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
