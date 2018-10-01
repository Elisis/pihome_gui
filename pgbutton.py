import pygame
from pygame.locals import *

pygame.font.init()
PGBUTTON_FONT = pygame.font.Font("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 14)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKGREY = (64, 64, 64)
LIGHTGREY = (212, 208, 200)
GREY = (128, 128, 128)

class PgButton(object):
	def __init__(self, rect = None, caption = "", bgcolor = LIGHTGREY, fgcolor = BLACK, font = None, normal = None, down = None, highlight = None):
		if rect is None:
			self._rect = pygame.Rect(0, 0, 30, 60)
		else:
			self._rect = pygame.Rect(rect)
		
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
		pygame.draw.line(self.surfaceNormal, DARKGREY, (1, h - 1), (w - 1, h - 1))
		pygame.draw.line(self.surfaceNormal, DARKGREY, (w - 1, 1), (w - 1, h - 1))
		pygame.draw.line(self.surfaceNormal, GREY, (2, h - 2), (w - 2, h - 2))
		pygame.draw.line(self.surfaceNormal, GREY, (w - 2, 2), (w - 2, h - 2))
		
		#Draw border for down button
		pygame.draw.rect(self.surfaceNormal, BLACK, pygame.Rect((0, 0, w, h)), 1) #Black border around everything
		pygame.draw.line(self.surfaceNormal, WHITE, (1, 1), (w - 2, 1))
		pygame.draw.line(self.surfaceNormal, WHITE, (1, 1), (1, h - 2))
		pygame.draw.line(self.surfaceNormal, DARKGREY, (1, h - 2), (1, 1))
		pygame.draw.line(self.surfaceNormal, DARKGREY, (1, 1), (w - 2, 1))
		pygame.draw.line(self.surfaceNormal, GREY, (2, h - 3), (2, 2))
		pygame.draw.line(self.surfaceNormal, GREY, (2, 2), (w - 3, 2))
		
		#Draw border for highlight button
		self.surfaceHighlight = self.surfaceNormal
		
	
	#Event callbacks
	def mouseClick(self, event):
		pass #This class is meant to be overriden
	
	def mouseEnter(self, event):
		pass #This class is meant to be overriden
		
	def mouseMove(self, event):
		pass #This class is meant to be overriden
		
	def mouseExit(self, event):
		pass #This class is meant to be overriden
	
	def mouseDown(self, event):
		pass #This class is meant to be overriden
	
	def mouseUp(self, event):
		pass #This class is meant to be overriden
		
	
	def handleEvent(self, eventObj):
		if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN) or not self._visible:
			#The button only cares about mouse-related events (or no events, if it is invisible)
			return []
			
		retVal = []
		
		hasExited = False
		if not self.mouseOverButton and self._rect.collidepoint(eventObj.pos):
			#If mouse has entered the button:
			self.mouseOverButton = True
			self.mouseEnter(eventObj)
			retVal.append('enter')
		
		elif self.mouseOverButton and not self._rect.collidepoint(eventObj.pos):
			#If mouse has exited the button:
			self.mouseOverButton = False
			hasExited = True #Call mouseExit() later, since we want mouseMove() to be handled before mouseExit()
			
		
		if self._rect.collidepoint(eventObj.pos):
			#If mouse event happened over the button:
			if eventObj.type == MOUSEMOTION:
				self.mouseMove(eventObj)
				retVal.append('move')
				
			elif eventObj.type == MOUSEBUTTONDOWN:
				self.buttonDown = True
				self.lastMouseDownOverButton = True
				self.mouseDown(eventObj)
				retVal.append('down')
		
		else:
			if eventObj.type in (MOUSEBUTTONUP, MOUSEBUTTONDOWN):
				#If an up/down happens off the button, then the next up won't cause mouseClick()
				self.lastMouseDownOverButton = False
		
		#Mouse up is handled whether or not it was over the button
		doMouseClick = False
		if eventObj.type == MOUSEBUTTONUP:
			if self.lastMouseDownOverButton:
				doMouseClick = True
			
			self.lastMouseDownOverButton = False
			
			if self.buttonDown:
				self.buttonDown = False
				self.mouseUp(eventObj)
				retVal.append('up')
				
			if doMouseClick:
				self.buttonDown = False
				self.mouseClick(eventObj)
				retVal.append('click')
				
				
		if hasExited:
			self.mouseExit(eventObj)
			retVal.append('exit')
			
		return retVal
		
	#Caption attributes
	def _propGetCaption(self):
		return self._caption
		
	def _propSetCaption(self, captionText):
		self.customSurfaces = False
		self._caption = captionText
		self._update()
		
	#Rect attributes
	def _propGetRect(self):
		return self._rect
		
	def _propSetRect(self, newRect):
		#Note that changing the attributes of the Rect won't update the button. You have to reassign the rect number.
		self._update()
		self._rect = newRect
	
	#Visibility attributes
	def _propGetVisible(self):
		return self._visible
		
	def _propSetVisible(self, setting):
		self._visible = setting
		
	#Foreground colour attributes
	def _propGetFgColor(self):
		return self._fgcolor
		
	def _propSetFgColor(self, setting):
		self.customSurfaces = False
		self._fgcolor = setting
		self._update()
		
	#Background colour attributes
	def _propGetBgColor(self):
		return self._bgcolor
		
	def _propSetBgColor(self, setting):
		self._customSurfaces = False
		self._bgcolor = setting
		self._update()
		
	#Font attributes
	def _propGetFont(self):
		return self._font
		
	def _propSetFont(self, setting):
		self.customSurfaces = False
		self._font = setting
		self._update()
		
	caption = property(_propGetCaption, _propSetCaption)
	rect = property(_propGetRect, _propSetRect)
	visible = property(_propGetVisible, _propSetVisible)
	fgcolor = property(_propGetFgColor, _propSetFgColor)
	bgcolor = property(_propGetBgColor, _propSetBgColor)
	font = property(_propGetFont, _propSetFont)
	font = property(_propGetFont, _propSetFont)