import pygame
 
 # subclasse de pygame.Sprite
class ClickableSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, callback):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.callback = callback
    #
    # self.rect faz um collider em torno da imagem 
    # pro point&click do mouse detectar
    # callback é a função a ser chamada quando for clicada
    #
 
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    print("chamandO")
                    self.callback()
 
