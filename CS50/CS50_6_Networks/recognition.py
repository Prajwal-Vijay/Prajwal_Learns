import numpy as np
import pygame
import sys
import tensorflow as tf
import time

model = tf.keras.models.load_model(sys.argv[1])

BLACK=(0,0,0)
WHITE=(255,255,255)

pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
OPEN_SANS = "assets/fonts/OpenSans-Regular.ttf"
smallFont = pygame.font.Font(OPEN_SANS, 20)
largeFont = pygame.font.Font(OPEN_SANS, 40)

ROWS, COLS = 28, 28

OFFSET = 20
CELL_SIZE = 10

handwriting = [[0]*COLS for _ in range(ROWS)] #Creates a list in list with given rows and columns

classification = None

while True:
    #Check For Game QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(BLACK)
    #Check for Mouse PRESS
    click,_,_ = pygame.mouse.get_pressed()
    if click == 1:
        mouse = pygame.mouse.get_pos()
    else:
        mouse = None
    #Draw each grid cell
    cells=[]
    for i in range(ROWS):
        row = []
        for j in range(COLS):
            rect=pygame.Rect(
                OFFSET+j*CELL_SIZE,
                OFFSET+i*CELL_SIZE,
                CELL_SIZE,CELL_SIZE
            )

            #If each cell has been written on, darken cell
            if handwriting[i][j]:
                channel = 255-(handwriting[i][j] * 255)
                pygame.draw.rect(screen, (channel,channel,channel), rect)
            else:
                pygame.draw.rect(screen,WHITE,rect)
            pygame.draw.rect(screen, BLACK, rect, 1)
            
            #Filling the cells with "ripple effect"
            if mouse and rect.collidepoint(mouse):
                handwriting[i][j] = 250/255
                if i+1 < ROWS:
                    handwriting[i+1][j] = 220/225
                if j+1 < COLS:
                    handwriting[i][j+1] = 220/225
                if i+1 < ROWS and j+1 < COLS:
                    handwriting[i+1][j+1] = 190/225    
    #Reset Button
    resetButton = pygame.Rect(
        30, OFFSET + ROWS*CELL_SIZE+30,
        100,30
    )
    resetText = smallFont.render("Reset", True, BLACK)
    resetTextRect = resetText.get_rect()
    resetTextRect.center = resetButton.center
    pygame.draw.rect(screen,WHITE, resetButton)
    screen.blit(resetText, resetTextRect)
    
    #Classify Button
    classifyButton = pygame.Rect(
        130 + 10, OFFSET + COLS*CELL_SIZE+30,
        100, 30
    )
    classifyText = smallFont.render("Classify", True, BLACK)
    classifyTextRect = resetText.get_rect()
    classifyTextRect.center = classifyButton.center
    pygame.draw.rect(screen, WHITE, classifyButton)
    screen.blit(classifyButton, classifyTextRect)
    
    #Reset Drawing
    if mouse and resetButton.collidepoint(mouse): #checks if mouse exists and if the collision point is within the range
        handwriting = [[0]*COLS for _ in range(ROWS)]
        classification = None
    
    #Generate Classification
    if mouse and classifyButton.collidepoint(mouse):
        classification = model.predict(
            [np.array(handwriting).reshape(1,28,28,1)]
        ).argmax()
        
    #Show classification if one exists
    if classification is not None:
        classificationText = largeFont.render(str(classification), True, WHITE)
        classificationRect = classificationText.get_rect()
        grid_size = OFFSET * 2 + CELL_SIZE * COLS
        classificationRect.center = (
            grid_size + ((width-grid_size)/2),
            100
        )
        screen.blit(classificationText, classificationRect)
        
    pygame.display.flip()