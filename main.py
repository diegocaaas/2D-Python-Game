import pygame
width, height = 500,500    
WIN = pygame.display.set_mode((width,height))

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()
if __name__ == "__main__":
    main()