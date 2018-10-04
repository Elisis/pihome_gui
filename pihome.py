#!/usr/bin/python2.7
import pygame
from pygame.locals import *
import time
import sys
import pgbutton
import datetime
import GIFImage
import os
import ptext

pygame.init()
pygame.font.init()
pygame.mouse.set_visible(0)

date = time.strftime("%d")

WIDTH = 800
HEIGHT = 480

GREY = pygame.Color(68, 68, 68)
LIGHTGREY = pygame.Color(169, 169, 169)
DARKGREY = pygame.Color(255, 255, 255)


bodyfont = pygame.font.Font("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 14)


def dateSuffix():
	digits = [int(digit) for digit in str(date)]
	
	if digits[-1] == 1:
		return "st"
	elif digits[-1] == 2:
		return "nd"
	elif digits[-1] == 3:
		return "rd"
	elif digits[-1] >= 4:
		return "th"
	elif digits[-1] == 0:
		return "th"

def init():
	running = True

def cleanup():
	pygame.quit()
	sys.exit()
	
def main_menu():
	
	global DISPLAYSURF
	DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME | pygame.DOUBLEBUF)
	

	quitButtonObj = pgbutton.PgButton((620, 0, 60, 30), "X")	
	timeButtonObj = pgbutton.PgButton((80, 60, 120, 60), "Time and Date")
	weatherButtonObj = pgbutton.PgButton((600, 60, 120, 60), "Weather")
	
	exitButtonObj = pgbutton.PgButton((740, 50, 40, 20))
	
	while True:
		for event in pygame.event.get():
			
			if 'click' in timeButtonObj.handleEvent(event):
				setup_time()
			
			if 'click' in weatherButtonObj.handleEvent(event):
				setup_weather()
			
			if 'click' in quitButtonObj.handleEvent(event):
				os.system("echo nutscatsdogs3187 | sudo -S shutdown now")
			
				
		pygame.Surface.fill(DISPLAYSURF, GREY)
		exitButtonObj.draw(DISPLAYSURF)
		timeButtonObj.draw(DISPLAYSURF)
		weatherButtonObj.draw(DISPLAYSURF)
		pygame.display.update()	
	 	
def setup_time():
	
	returnButtonObj = pgbutton.PgButton((600, 60, 60, 30), "Return")
	
	while True:
		for event in pygame.event.get():
			
			if 'click' in returnButtonObj.handleEvent(event):
				main_menu() 
		pygame.Surface.fill(DISPLAYSURF, GREY)
		returnButtonObj.draw(DISPLAYSURF)
		#currentTime = datetime.strptime("%A, %d %B, %H:%M:%S")
		currentTime = time.strftime("%A, %d" + dateSuffix() + " %B, %H:%M:%S")
		ptext.draw("Current Time: " + currentTime + ".", (20, 100), fontsize = 50)	
		pygame.display.update()

def setup_weather():
	while True:
		
		os.system("wget -N -o /dev/null ftp://ftp.bom.gov.au/anon/gen/radar/IDR014.gif")
		radar = GIFImage.GIFImage("IDR014.gif")

		for event in pygame.event.get():
			if event.type == QUIT:
				cleanup()
			
			#if
				
		pygame.Surface.fill(DISPLAYSURF, GREY)
		radar.render(DISPLAYSURF, (140, -10))
		pygame.display.update()
		

if __name__ == "__main__":
	init()
	main_menu()
	raw_input()
	setup_time()
	raw_input()

