#!/usr/bin/python2.7
import pygame
from pygame.locals import *
import time
import sys

pygame.init()
pygame.font.init()

WIDTH = 800
HEIGHT = 480

GREY = pygame.Color(68, 68, 68)
LIGHTGREY = pygame.Color(169, 169, 169)

bodyfont = pygame.font.Font("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 14)


def init():
	running = True

def cleanup():
	pygame.quit()
	
def main_menu():
	
	global DISPLAYSURF
	DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
	
	TIMEBUTTON = bodyfont.render("Time", False, (20, 20, 0))
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				cleanup()
		
		pygame.Surface.fill(DISPLAYSURF, GREY)
		pygame.draw.rect(DISPLAYSURF, LIGHTGREY, [20, 20, 80, 40])
		DISPLAYSURF.blit(TIMEBUTTON, (45, 30))
		pygame.display.update()
	 	
def setup_time():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				cleanup()
		pygame.Surface.fill(DISPLAYSURF, pygame.Color(255, 255, 255))
		TEXTSURF = bodyfont.render("Some Text", False, (0, 0, 0))
		DISPLAYSURF.blit(TEXTSURF, (0, 0))
		pygame.display.flip()



'''class Button(object):
	
	def __init__(self, rect, colour, function, **kwargs):
		self.rect = pygame.Rect(rect)
		self.colour = colour
		self.function = function
		self.clicked = False
		self.hovered = False
		self.hover_text = None
		self.clicked_text = None
		self.process_kwargs(kwargs)
		self.render_text()
	
	def process_kwargs(self, kwargs):
		
		settings = {
			"text" : None,
			"font" : pygame.font.Font(None, 16),
			"call_on_release" : True,
			"hover_colour" : None,
			"clicked_colour" : None,
			"font_colour" : pg.Color("white"),
			"hover_font_colour" : None,
			"clicked_font_colour" : None,
			"click_sound" : None,
			"hover_sound" : None
		}
		
		for kwarg in kwargs:
			if kwarg in settings:
				settings[kwarg] = kwargs[kwarg]
			
			else:
				raise AttributeError("Button has no keyword: {}".format(kwarg)
		
		self.__dict__.update(settings)
		
	def render_text(self):
        """Pre render the button text."""
        if self.text:
            if self.hover_font_colour:
                colour = self.hover_font_colour
                self.hover_text = self.font.render(self.text,True,colour)
            if self.clicked_font_colour:
                colour = self.clicked_font_colour
                self.clicked_text = self.font.render(self.text,True,colour)
            self.text = self.font.render(self.text,True,self.font_colour)
            
	def check_event(self,event):
        """The button needs to be passed events from your program event loop."""
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.on_release(event)

    def on_click(self,event):
        if self.rect.collidepoint(event.pos):
            self.clicked = True
            if not self.call_on_release:
                self.function()

    def on_release(self,event):
        if self.clicked and self.call_on_release:
            self.function()
        self.clicked = False

    def check_hover(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            if not self.hovered:
                self.hovered = True
                if self.hover_sound:
                    self.hover_sound.play()
        else:
            self.hovered = False

    def update(self,surface):
        """Update needs to be called every frame in the main loop."""
        colour = self.colour
        text = self.text
        self.check_hover()
        if self.clicked and self.clicked_colour:
            colour = self.clicked_colour
            if self.clicked_font_colour:
                text = self.clicked_text
        elif self.hovered and self.hover_colour:
            colour = self.hover_colour
            if self.hover_font_colour:
                text = self.hover_text
        surface.fill(pg.Color("black"),self.rect)
        surface.fill(colour,self.rect.inflate(-4,-4))
        if self.text:
            text_rect = text.get_rect(center=self.rect.center)
            surface.blit(text,text_rect)


'''

class Main:
	def __init__(self):
		self._running = True
		self._display_surf = None
		self.size = self.weight, self.height = 800, 480 
	
	def on_init(self):
		pygame.init()
		
		self._display_surf = display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		time_button = pygame.draw.rect(self._display_surf, (0, 0, 240), (150, 90, 100, 50))
		self._running = True
		
	def on_event(self, event):
		
		pygame.Surface.fill(self._display_surf, GREY)
		pygame.draw.rect(self._display_surf, LIGHTGREY, [20, 20, 20, 20])
		
		display.update()
		if event.type == pygame.QUIT:
			self._running = False
		
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pos() >= (150, 230):
				pygame.quit()
	
	def on_loop(self):
		pass
		
	def on_render(self):
		pass
	
	def on_cleanup(self):
		pygame.quit()
		
	def on_execute(self):
		
		if self.on_init() == False:
			self._running = False
			
		while (self._running):
			
			mouse = pygame.mouse.get_pos()
			
			for event in pygame.event.get():
				self.on_event(event)
			
			self.on_loop()
			self.on_render()
			
			
		
		self.on_cleanup()
			
					
if __name__ == "__main__":
	init()
	main_menu()
	raw_input()
	setup_time()
	raw_input()

