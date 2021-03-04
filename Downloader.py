import pytube
from pytube import YouTube
import os
import sys
import argparse
import time
red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
cy='\033[095m'
cya='\033[035m'
maku='\033[90m'
fari='\033[97m'
def hauka():
	os.system("clear")
	print(yellow+bold)
	os.system("figlet U-danbaiwa.")
	print(green+bold+"\t\t\tVersion:"+cyan+bold+"2.0.0")
	print(cya+bold+"\t\tGithub:"+cyan+bold+"www.github.com/U-danbaiwa")
	print("\n\n")
hauka()
def banner():
	p=("\t\t #############################\n\t"+yellow+"\t #\t"+cya+" YOUTUBE VIDEOS"+yellow+"\t     #\n\t\t #\t  "+cyan+bold+" DOWNLOADER"+yellow+"\t     #\n\t\t #\t     CODED\t     #\n\t\t #\t  "+green+bold+" U-danbaiwa"+yellow+"\t     #\n\t\t #     HAH! HAH!! HAH!!!     #\n\t\t"+green+" #############################")
	for line in p:
		sys.stdout.flush()
		time.sleep(0.03)
		print(line,end="")
		
	
banner()
def ya():
	print("\n\n")
	try:
		ba=input("Enter Video Url/Link: "+yellow+bold)
		print("\n\t\t\tPlease wait...")
		time.sleep(5)
		print("")
		print(green+bold+"[-] YOU START DOWNLOAD AT: "+red+bold+time.strftime("%H:%M:%S"))
		print("")
		print(yellow+bold+"{+} Starting Downloading...")
		you=pytube.YouTube(ba)
		vid=you.streams.first()
		vid.download("/sdcard")
		print("\n")
		print(green+bold+"[-] COMPLETE DOWNLOAD AT: "+red+bold+time.strftime("%H:%M:%S"))
		print(yellow+bold)
		os.system("figlet Complete...")
		print("\n")
		ta="[+] Open Your File Manager You will See Your Video BRO [+]"
		for line in ta:
			sys.stdout.flush()
			time.sleep(0.1)
			print(cya+bold+line,end="")
		print("\n")
		info=input("[-] Do You Want See Video Info?? Y / N: ")
		if info=="y" or info=="yes" or info=="Y":
			fo=YouTube(ba)
			print("\n")
			print(green+bold+"[+] VIDEO TITLE: "+yellow+bold+fo.title)
			print("")
			print(green+bold+"[+] VIDEO ID: "+yellow+bold+fo.video_id)
			print("")
			print(green+bold+"[+] VIDEO DESCRIPTION: "+yellow+bold+fo.description)
			print("")
			print(green+bold+"[+] VIDEO LENGTH: "+yellow+bold,fo.length)
			print("")
			print(green+bold+"[+] VIDEO THUMBNAIL URL/LINK: "+yellow+bold,fo.thumbnail_url)
			print("")
			print(green+bold+"[+] VIDEO VIEWS: "+yellow+bold,fo.views)
			print("")
			print(green+bold+"[+] VIDEO RATING: "+yellow+bold,fo.rating)
			print("")
			print(green+bold+"[+] VIDEO AGE RESTRICTED: "+yellow+bold,fo.age_restricted)
			print("")
		else:
			print("sorry")
	except Exception:
		print("")
		print("\tSOMETHING WRONG WITH"+fari+bold+" LINK"+cya+"/"+fari+bold+"INTERNET CONNECTION")
	
	
ya()
def re():
	print("\n\n")
	retu=input("Do You Want Continue Y for [yes] N for [no]: ")
	if retu=="y" or retu=="Y" or retu=="yes":
		hauka()
		banner()
		ya()
		re()
	else:
		print("\n")
		os.system("toilet See You")
		sys.exit()
re()
		
	