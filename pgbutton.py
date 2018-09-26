import pygame
from pygame.locals import *

pygame.font.init()
PGBUTTON_FONT = pygame.font.Font("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 14)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKGREY = (64, 64, 64)
LIGHTGREY = (128, 128, 128)

class PgButton(object):
	def __init__(self, rect = None, caption = "", bgcolor = LIGHTGREY, fgcolor = BLACK, font = None, normal = None, down = None, highlight = None):
		if rect is None:
			self._rect = pygame.Rect(0, 0, 30, 60)
		else:
			self._rect = pygame.Rect(object)
		
		self._caption = caption
		self._bgcolor = bgcolor
		self._fgcolor = fgcolor
		
		if font is None:
			self._font = PGBUTTON_FONT
		else:
			self._font = font
			
		#Tracks the state of the button
		self.buttonDown = False
		self.mouseOverButton = False
		self.lastMouseDownOverButton = False
		self._visible = True
		self.customSurfaces = False
		
		if normal is None:
			#Create the surfaces for a text button
			self.surfaceNormal = pygame.Surface(self._rect.size)
			self.surfaceDown = pygame.Surface(self._rect.size)
			self.surfaceHighlight = pygame.Surface(self._rect.size)
			self._update()
		else:
			#Create the surfaces for a custom image button
			self.setSurfaces(normal, down, highlight)
			
	def setSurfaces(self, normalSurface, downSurface = None, highlightSurface = None):
		'''Switch the button to a custom image type of button (rather than a
		text button). You can specify either a pygame.Surface object or a
		string of a filename to load for each of the three button appearence
		states'''
		
		if downSurface is None:
			downSurface = normalSurface
		
		if highlightSurface is None:
			hightlightSurface = normalSurface
		
		if type(normalSurface) == str:
			self.origSurfaceNormal = pygame.image.load(normalSurface)
		
		if type(downSurface) == str:
			self.origSurfaceDown = pygame.image.load(downSurface)	
		 
		if type(highlightSurface) == str:
			self.origSurfaceHighlight = pygame.image.load(highlightSurface)
			 
		
		if self.origSurfaceNormal.get_size() != self.origSurfaceDown.get_size() != self.origSurfaceHighlight.get_size():
			raise Exception("Incorrect sizes for button surfaces")
			
		
		self.surfaceNormal = self.origSurfaceNormal
		self.surfaceDown = self.origSurfaceDown
		self.surfaceHighlight = self.origSurfaceHighlight
		self.customSurfaces = True
		self._rect = pygameRect((self._rect.left, self._rect.top, self.surfaceNormal.get_width(), self.surfaceNormal.get_height()))
		
	def draw(self, surfaceObj):
		#Blit the current button's appearence to the surface object.
		if self._visible:
			if self.buttonDown:
				surfaceObj.blit(self.surfaceDown, self._rect)
			elif self.mouseOverButton:
				surfaceObj.blit(self.surfaceHighlight, self._rect)
			else:
				surfaceObj.blit(self.surfaceNormal, self._rect)
				
	def _update(self):
		#Redraw the button's Surface object. Call this method when the button has changed appearence.
		if self.customSurfaces:
			self.surfaceNormal = pygame.transform.smoothscale(self.origSurfaceNormal, self._rect.size)
			self.surfaceDown = pygame.transform.smoothscale(self.origSurfaceDown, self._rect.size)
			self.surfaceHighlight = pygame.transform.smoothscale(self.origSurfaceHighlight, self._rect.size)
			return
			
		w = self._rect.width
		h = self._rect.height
		
		#Fill background colour for all buttons
		self.surfaceNormal.fill(self.bgcolor)
		self.surfaceDown.fill(self.bgcolor)
		self.surfaceHighlight.fill(self.bgcolor)
		
		#Draw caption text for all buttons
		captionSurf = self._font.render(self._caption, True, self.fgcolor, self.bgcolor)
		captionRect = captionSurf.get_rect()
		captionRect.center = int(w / 2), int(h / 2)
		
		self.surfaceNormal.blit(captionSurf, captionRect)
		self.surfaceDown.blit(captionSurf, captionRect)
		
		#Draw border for normal button
		pygame.draw.rect(self.surfaceNormal, BLACK, pygame.Rect((0, 0, w, h)), 1) #Black border around everything
		pygame.draw.line(self.surfaceNormal, WHITE, (1, 1), (w - 2, 1))
		pygame.draw.line(self.surfaceNormal, WHITE, (1, 1), (1, h - 2))
		pygame.draw.line(self.)
		