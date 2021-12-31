# imports for Arduino
import serial
from serial import Serial

def getButtonPush(arduino):
    while True:
        data = arduino.readline(1000)
        decodedData = data.strip().decode('UTF-8')
        return(decodedData)

def main():
    try:
        arduino = serial.Serial('COM3', 9600)
    except:
        print("Failed to connect to Arduino")
        quit()

    print('Welcome to the Adventure of Hurricane Preparation')
    ans = print('The weather outside isnt looking good. What should we do? Turn on the news or watch a movie? \n')
    ans = getButtonPush(arduino)

    if str(ans) == 'Left':
        print('Local News Channel 4 alerts locals of a hurricane watch is to arrive in 48 hours.\n\n')
        ans2 = print('Do you Enjoy the nice weather while it lasts or Get supplies from the grocery store? \n')
        ans2 = getButtonPush(arduino)

        if str(ans2) == 'Left':
            print('While enjoying the nice weather at the beach, you get a nervous feeling about the upcoming storm.\n\n')
            ans3 = print('Do you ignore the feeling and collect seashells or go home to review the evacuation plan with your family\n')
            ans3 = getButtonPush(arduino)

            if str(ans3) == 'Right':
                print('While talking to your family, you agree it is a good plan to keep a packed bag by the door just in case of an early evacuation.')
                print('You turn on the local news again and they warn us the hurricane is to arrive in 36 hours. This time the alert is a warning, and not a watch\n\n')
                ans4 = print('You wonder what the difference is between a hurricane watch and a hurricane warning, do you look up the difference online or assume the definitions are interchangable? \n')
                ans4 = getButtonPush(arduino)

                if str(ans4) == 'Left':
                    print('The CDC states that a hurricane watch is just the the conditions of a hurricane are possible in the area.')
                    print('And a hurricane warning is much more serious, meaning the conditions are expected.\n')

                    print('It is now 24 hours before the hurricane. We are not sure if we will have to evacuate or not.')
                    print('You check your car and you have a little over half a tank of gas.\n')
                    ans5 = print('Do you stay in because the gas stations will be packed and it will take up too much time or go anyway to play it safe? \n\n')
                    ans5 = getButtonPush(arduino)
                    
                    if str(ans5) == "Right":
                        print('I wasted three hours driving around trying to find a gas station that was not too busy, but I finally have a full tank.')
                        print('18 hours until the hurricane\n')
                        ans6 = print('Do I start to move the garbage cans inside or go to the hardwood store to buy plywood\n\n')
                        ans6 = getButtonPush(arduino)

                        if str(ans6) == "Right":
                            print('I was in luck! They had the perfect amount to board up all my windows! I wish I had storm shutters though.\n')
                            ans7 = print('Do I go online to order hurricane shutters asap for the next hurricane or board up the windows before we forget? \n\n')
                            ans7 = getButtonPush(arduino)

                            if str(ans7) == "Right":
                                print('Boarding up the windows right now was a great choice since we have such little time.')
                                print('12 hours until the hurricane\n')

    arduino.close()

if __name__ == "__main__":
    main()