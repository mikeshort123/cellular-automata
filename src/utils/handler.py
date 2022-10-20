import pygame, json

class Handler():


    def __init__(self):

        with open("res/keybinds.json", encoding="utf8") as f:
            self.key_map = json.load(f)

        self.key_list = {
            self.key_map[i] : False for i in self.key_map
        }

        self.key_changes = []

        self.mouse_pos = (0, 0)

    def reset(self):
        self.key_changes = []


    def get_key_pressed(self,key):

        return self.key_list[self.key_map[key]]


    def get_key_changed(self,key):

        code = self.key_map[key]
        return code in self.key_changes


    def get_mouse_pos(self):

        return self.mouse_pos


    def handle_event(self,e):

        if e.type == pygame.KEYDOWN:
            self.set_key(e.unicode, True)

        if e.type == pygame.KEYUP:
            self.set_key(e.unicode, False)

        if e.type == pygame.MOUSEBUTTONDOWN:
            self.set_key("mb" + str(e.button), True)

        if e.type == pygame.MOUSEBUTTONUP:
            self.set_key("mb" + str(e.button), False)

        if e.type == pygame.MOUSEMOTION:
            self.mouse_pos = e.pos


    def set_key(self, key, mode):
        if key in self.key_list:
            self.key_list[key] = mode

            if mode: self.key_changes.append(key)
