import pygame 


class clickableSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, callback, normalImage, clickedImage):
        super().__init__()
        self.clickedImage = clickedImage
        self.normalImage = normalImage

        self.image = normalImage
        self.rect = self.image.get_rect()
        self.rect.x = x #type:ignore
        self.rect.y = y #type:ignore
        self.callback = callback
        self.isClicked = False

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos): #type:ignore
                    self.callback()

class light(pygame.sprite.Sprite):
    def __init__(self, image, x, y, onImage, offImage):
        super().__init__()
        self.image = onImage
        self.onImage = onImage
        self.offImage = offImage
        self.rect = self.image.get_rect()
        self.rect.x = x #type:ignore
        self.rect.y = y #type:ignore

def on_click(spriteInstance, lightInstance):
    spriteInstance.isClicked = not spriteInstance.isClicked
    if spriteInstance.isClicked:
       spriteInstance.image = spriteInstance.clickedImage
       lightInstance.image = lightInstance.offImage
    else:
        spriteInstance.image = spriteInstance.normalImage
        lightInstance.image = lightInstance.onImage

pygame.init()
canvas = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Space Launch Simulator")

normalImage = pygame.image.load('sprites/Buttons_0002.png').convert_alpha()
clickedImage = pygame.image.load('sprites/Buttons_0001.png').convert_alpha()
onLight = pygame.image.load('sprites/OnAndOffLight_0001.png').convert_alpha()
offLight = pygame.image.load('sprites/OnAndOffLight_0002.png').convert_alpha()

powerLight = light(pygame.Surface((100, 100)), 452, 430, onLight, offLight)
lightgroup = pygame.sprite.GroupSingle(powerLight)

sprite = clickableSprite(pygame.Surface((100, 100)), 436,468, lambda: on_click(sprite, powerLight), normalImage, clickedImage)
group = pygame.sprite.GroupSingle(sprite)


running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    group.update(events)
    canvas.fill((0, 0, 0))
    lightgroup.draw(canvas)
    group.draw(canvas)
    
    pygame.display.update()

pygame.quit()