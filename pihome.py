#/usr/bin/python2.7
import pygame
from pygame.locals import *
import time
import sys
import pgbutton
import datetime
import GIFImage
import os
import ptext
from sense_hat import SenseHat
import forecastio

api_key = "3c8457364063f406ccc3ce8e71861dc9"
lat = "-37.907910"
lng = "145.020583" 

forecast = forecastio.load_forecast(api_key, lat, lng)

sh = SenseHat()

weather_api = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=melbourne"

pygame.init()
pygame.font.init()
pygame.mouse.set_visible(0)

date = time.strftime("%d")

WIDTH = 800
HEIGHT = 480

GREY = pygame.Color(68, 68, 68)
LIGHTGREY = pygame.Color(169, 169, 169)
DARKGREY = pygame.Color(255, 255, 255)

sh.clear()

bodyfont = pygame.font.Font("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 14)


def dateSuffix():
	digits = [int(digit) for digit in str(date)]

	if digits[-2] == 1:
		return "th"
	elif digits[-1] == 1 and digits[-2] != 1:
		return "st"
	elif digits[-1] == 2 and digits[-2] != 1:
		return "nd"
	elif digits[-1] == 3 and digits[-2] != 1:
		return "rd"
	elif digits[-1] >= 4 and digits[-2] != 1:
		return "th"
	elif digits[-1] == 0:
		return "th"

def cleanup():
	pygame.quit()
	sys.exit()
	
def main_menu():
	
	global DISPLAYSURF
	DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME | pygame.DOUBLEBUF)
	

	#quitButtonObj = pgbutton.PgButton((620, 0, 60, 30), "X")	
	timeButtonObj = pgbutton.PgButton((80, 60, 120, 60), "Time and Date")
	weatherButtonObj = pgbutton.PgButton((600, 60, 120, 60), "Weather")
	conditionsButtonObj = pgbutton.PgButton((340, 210, 120, 60), "Conditions") 	
	
	exitButtonObj = pgbutton.PgButton((740, 50, 40, 20), "X")
	
	while True:
		for event in pygame.event.get():
			
			if 'click' in timeButtonObj.handleEvent(event):
				setup_time()
			
			if 'click' in weatherButtonObj.handleEvent(event):
				setup_weather()
			
			if 'click' in exitButtonObj.handleEvent(event):
				os.system("echo nutscatsdogs3187 | sudo -S shutdown now")
			
			if 'click' in conditionsButtonObj.handleEvent(event):
				current_conditions()
				
		pygame.Surface.fill(DISPLAYSURF, GREY)
		
		exitButtonObj.draw(DISPLAYSURF)
		timeButtonObj.draw(DISPLAYSURF)
		weatherButtonObj.draw(DISPLAYSURF)
		conditionsButtonObj.draw(DISPLAYSURF)
		
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

def setup_weather_with_radar():
	
	returnButtonObj = pgbutton.PgButton((600, 60, 60, 30), "Return")

	while True:
		
		
		
		os.system("wget -N -o /dev/null ftp://ftp.bom.gov.au/anon/gen/radar/IDR014.gif")
		radar = GIFImage.GIFImage("IDR014.gif")	

		for event in pygame.event.get():
			
			if 'click' in returnButtonObj.handleEvent(event):
				setup_weather()
			
			#if
				
		pygame.Surface.fill(DISPLAYSURF, GREY)
		returnButtonObj.draw(DISPLAYSURF)
		radar.render(DISPLAYSURF, (140, -10))
		pygame.display.update()
		
def setup_weather():	
	
	radarToggleButtonObj = pgbutton.PgButton((600, 100, 120, 60), "Show Radar")
	returnButtonObj = pgbutton.PgButton((600, 60, 60, 30), "Return")
	
	while True:
		
		byHour = forecast.hourly()

		for event in pygame.event.get():
			
			if 'click' in radarToggleButtonObj.handleEvent(event):
				setup_weather_with_radar()

			if 'click' in returnButtonObj.handleEvent(event):
				main_menu()

		pygame.Surface.fill(DISPLAYSURF, GREY)
		ptext.draw("The current predicted wheather is " + byHour.summary, (20, 100))
		radarToggleButtonObj.draw(DISPLAYSURF)
		returnButtonObj.draw(DISPLAYSURF)
		pygame.display.update()	

def current_conditions():
	
	returnButtonObj = pgbutton.PgButton((600, 60, 60, 30), "Return")	
	
	while True:
		
		humidity = sh.get_humidity()

		for event in pygame.event.get():
		
			if 'click' in returnButtonObj.handleEvent(event):
				main_menu()
	
		pygame.Surface.fill(DISPLAYSURF, GREY)
		returnButtonObj.draw(DISPLAYSURF)
		ptext.draw("Humidity: " + humidity, (100, 20))
		pygame.display.update()		
			



if __name__ == "__main__":
	main_menu()


