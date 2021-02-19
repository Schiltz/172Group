'''
Created on Feb 19, 2021

@author: jonathanschiltz
'''
"""
    Create a display surface and caption it. Download an image of a small ball and
    import that image into your program.
    Create a horizontal ground of some thickness (something similar to what we saw
    in the aliens game). Let the initial position of this ball be on this ground.
    
    Write code such that the ball bounces between this ground and the top boundary
    of your display surface. That is, the ball keeps bouncing up and down and up and
    down and (you guessed it ;-))
    
    Note: Try to play around with colors as well. Also play with the frame speed.
    Hint: Recall that any action can be performed by writing code for various events.
            How to bounce the ball once it hits the ground or the boundary?
"""





def main():
    import sys, pygame
    pygame.init()
    ##import and init pygame

    size = width, height = 800, 600
    speed = [0, -2]
    ##set size and speed variables
    
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    orange = (255, 140, 0)
    ##bring in color variables for easy switching

    gameScreen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ex1 Game")
    ##create display surface and give a caption

    ball = pygame.image.load("smallBall.png")
    ball = pygame.transform.scale(ball, (100, 100))
    ballrect = ball.get_rect()
    ##import ball image, scale, and get rect values
    
    ballrect.x = 335
    ballrect.y = 450
    ##set starting ball position
    
    FPS = 60
    myClock = pygame.time.Clock()
    ##create FPS controls
    

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            ##exit statement

        ballrect = ballrect.move(speed)
        ##set ball into movement
        if ballrect == (335, 450, 100, 100):
            speed[1] = -speed[1]
        if ballrect == (335, 0, 100, 100):
            speed[1] = -speed[1]
        ##if statements to check if ball is at edges and reverse direction if so
            
        myClock.tick(FPS)
        ##implementation of FPS controls
        
        gameScreen.fill(black)
        pygame.draw.rect(gameScreen, blue, [0, 550, 800, 50], 0)
        gameScreen.blit(ball, ballrect)
        pygame.display.flip()
        ##color in display surface, create a ground, and update image location
    
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()