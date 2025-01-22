import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from logic import *

def main():
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    logic = Logic(0, 3)
    font = pygame.font.Font(None, FONT_SIZE)
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (updateable, drawable, shots)
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    

    while True:
        screen.fill((0, 0, 0))
        number = logic.score
        lives = logic.lives
        for object in updateable:
            object.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                logic.die()
                player.reset()

                if lives <= 0:
                    print("Game over!")
                    sys.exit()
            for shot in shots:    
                if asteroid.collision(shot):
                    logic.add_score(1)
                    asteroid.split()
                    shot.kill()
                
        
        # Render the number as text
        text_surface_number = font.render(f"Score: {number}", True, (255, 255, 255))
        text_surface_lives = font.render(f"Lives: {lives}", True, (255, 255, 255))



        # Blit (draw) the text to the screen
        screen.blit(text_surface_number, (50, 100))  # Position (x, y)
        screen.blit(text_surface_lives, (50, 50))

        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
