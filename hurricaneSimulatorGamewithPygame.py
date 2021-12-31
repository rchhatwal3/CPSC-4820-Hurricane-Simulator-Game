# imports for Arduino
import serial
from serial import Serial

# imports for PyGame
import pygame
from pygame.locals import *
from pygame import font

pygame.init()

# defining RGB
white = (255, 255, 255)
black= (0, 0, 0)

# assigning screen dimensions
X = 1600
Y = 1000

display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Adventures of Hurricane Preparation")

imagePath = r'C:/Users/Ramneek/Documents/Code_Projects/CPSC-4820-Hurricane-Simulator-Game/assets/hurricane.jpg'
imageTextUpper = "Welcome to the Adventure of Hurricane Preparation"
imageTextLower = "The weather outside isnt looking good. What should we do? Turn on the news or watch a movie?"

image = pygame.image.load(imagePath).convert()
image = pygame.transform.scale(image, (1600, 750))

font = pygame.font.Font('freesansbold.ttf', 30)
textUpper = font.render(imageTextUpper, True, black, white)
textLower = font.render(imageTextLower, True, black, white)


leftTextList = ["Local News Channel 4 alerts locals of a hurricane watch is to arrive in 48 hours.", "While enjoying the nice weather at the beach, you get a nervous feeling about the upcoming storm."]
leftQuestionList = ["Do you Enjoy the nice weather while it lasts or Get supplies from the grocery store?", "Do you ignore the feeling and collect seashells or go home to review the evacuation plan with your family"]
rightTextList = ["You turn on the local news again and they warn us the hurricane is to arrive in 36 hours. This time the alert is a warning, and not a watch", "18 hours until the hurricane"]
rightQuestionList = ["You wonder what the difference is between a hurricane watch and a hurricane warning, do you look up the difference online or assume the definitions are interchangable?", "Do I start to move the garbage cans inside or go to the hardwood store to buy plywood"]
questionImageDict = {
    "Do you Enjoy the nice weather while it lasts or Get supplies from the grocery store?": r"C:/Users/Ramneek/Documents/Code_Projects/CPSC-4820-Hurricane-Simulator-Game/assets/hurricaneAlert.jpg",
    "Do you ignore the feeling and collect seashells or go home to review the evacuation plan with your family": r"C:/Users/Ramneek/Documents/Code_Projects/CPSC-4820-Hurricane-Simulator-Game/assets/nervousFeeling.jpg",
    "You wonder what the difference is between a hurricane watch and a hurricane warning, do you look up the difference online or assume the definitions are interchangable?": r"C:/Users/Ramneek/Documents/Code_Projects/CPSC-4820-Hurricane-Simulator-Game/assets/watchvswarning.jpg",
    "Do I start to move the garbage cans inside or go to the hardwood store to buy plywood": r"C:/Users/Ramneek/Documents/Code_Projects/CPSC-4820-Hurricane-Simulator-Game/assets/18hours.jpg"
}

def getButtonPush(arduino):
    while True:
        data = arduino.readline(1000)
        decodedData = data.strip().decode('UTF-8')
        return(decodedData)

def gameEvents(arduino, direction):
    global imagePath
    global imageTextLower
    global imageTextUpper
    global image
    global font
    global textUpper
    global textLower

    if "Left":
        imageTextLower = leftQuestionList.pop(0)
        imageTextUpper = leftTextList.pop(0)

    elif "Right":
        imageTextLower = rightQuestionList.pop(0)
        imageTextUpper = rightTextList.pop(0)

    iPath = questionImageDict[imageTextLower]
    imagePath = iPath

    image = pygame.image.load(imagePath).convert()
    image = pygame.transform.scale(image, (1600, 750))

    font = pygame.font.Font('freesansbold.ttf', 30)
    textUpper = font.render(imageTextUpper, True, black, white)
    textLower = font.render(imageTextLower, True, black, white)


def main():
    try:
        arduino = serial.Serial('COM3', 9600)
    except:
        print("Failed to connect to Arduino")
        quit()

    while True:
        display_surface.fill(white)
        display_surface.blit(image, (0,125))
        display_surface.blit(textUpper, (0,50))
        display_surface.blit(textLower, (0, 900))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    gameEvents(arduino, "Left")
                elif event.key == K_RIGHT:
                    gameEvents(arduino, "Right")
        pygame.display.update()

    arduino.close()

if __name__ == "__main__":
    main()
