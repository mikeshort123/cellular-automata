import pygame, json

class Handler():


    def __init__(self):

        self.events = {}

    def register_event(self, event, target):
        self.events[event] = target



    def handle_event(self,e):

        if e.type == pygame.KEYDOWN:
            self.trigger_event("KEYDOWN_" + str(e.unicode))

        if e.type == pygame.KEYUP:
            self.trigger_event("KEYUP_" + str(e.unicode))

        if e.type == pygame.MOUSEBUTTONDOWN:
            self.trigger_event("KEYDOWN_" + "mb" + str(e.button))

        if e.type == pygame.MOUSEBUTTONUP:
            self.trigger_event("KEYUP_" + "mb" + str(e.button))


    def trigger_event(self, event):
        if event in self.events:
            self.events[event]()
