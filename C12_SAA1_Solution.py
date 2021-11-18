# Import "pygame" modules 
import pygame

# Initialize "pygame"
pygame.init() 

# Create a game screen and set its title 
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Student Additional Activity 1")

# Game loop
carryOn = True
while carryOn:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            carryOn = False
    
    # Student Additional Activity 1: Display tree, hut and cloud images
    # Load the images
    tree = "tree.png"
    treeImg = pygame.image.load(tree).convert_alpha()
    
    hut = "hut.png"
    hutImg = pygame.image.load(hut).convert_alpha()
    hutImg = pygame.transform.smoothscale(hutImg,(300,200))
    
    cloud = "cloud.png"
    cloudImg = pygame.image.load(cloud).convert_alpha()
    cloudImg = pygame.transform.smoothscale(cloudImg,(500,150))

    # Display the images
    screen.blit(treeImg,(50,300))
    screen.blit(hutImg,(200,250))
    screen.blit(cloudImg,(50,50))

    # Update the contents of the display
    pygame.display.flip()

# On the occurence of "pygame.QUIT" event close the game screen
pygame.quit()