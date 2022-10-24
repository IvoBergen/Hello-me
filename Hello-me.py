
Yes = ['Yes', 'yes', 'Y', 'y']
No = ['No', 'no', 'N', 'n']

def beforewestart():
    print('Hello and welcome to this text based story game! A few rules/ things to do while playing! You can only answer with: Yes, yes, Y, y. or No, no, N, n. the story is not that long so have fun!')
    choice = input('Are you ready: ')
    if choice in Yes:
        print('Here we go!')
        intro()
    elif choice in No:
        print('Come lets go you baby')
        intro()
            
def intro():
    print('You wake up in an unknown location. You look around and see nothing familiar around you. The last thing you remember is: that you were walking through your home town (New York) and suddenly everything went black. You remember that your name is: Alex Northman. After you started walking down a pathway you saw up ahead, you encounter a unknown creature that is in the middle of the pathway… What do you do? Do you want to try to talk with it. Yes or No? ')
    choice = input('Yes or No: ')
    

def tekst1():
    print("You try to communicate with the creature after you walk closer you see that it is small at least smaller than a human. It looks like nothing you have ever seen before, or maybe a little bit like and dwarf you have read about in books. When you are a two meters away from the creature you say Hi the creature turn around and you see its face it is covered in food it looks like he was eating tomato’s and some other vegetables. The creature looks at you with a terrified face and goes: wh-what are you? I have never seen such a species before. You tell the creature a short story about how you got to the place after you finish your story you ask the creature if it had a name and were you are. The creature responds with: m-my name is Jennifer and you are in the land of the lost it is a world beneath the surface of the earth. You were shocked to find out that you are inside the earth… after a little while you ask if Jennifer if she has a place to live. She responds with yes I do! It is not to far away from here, would you like to come over to maybe figure out how to get back up to the surface… Are you going with Jennifer to her house Yes or No?")
    choice = input('Yes or No: ')
    if choice in Yes:
        tekst5()
    elif choice in No:
        tekst2()

def tekst2():
    print("After rejecting Jennifer’s offer you ask if there is anything dangerous in this world? Jennifer responds with a nervous reaction: Why do you think this is the most peaceful place to ever live! I never want to leave from this place. You doubt Jennifer for a split second but you don’t think to much of it. You ask if Jennifer knows a good place to set up a camp and she responds with telling you to go to the west because to the east there are a lot of mountains to climb and that is not useful while travelling. Do you go west (yes) or east (no)?")
    choice = input('Yes or No: ')
    if choice in Yes:
        tekst6()
    elif choice in No:
        tekst3()

def tekst3():
    print('You decide to go east to get to a higher point for a better view of the lands. After a hike for about twenty minutes you see the cliff edge of the mountain. ')
    tekst4()
    
def tekst4():
    print("After a little bit of thinking you decided to go anyways. You climb and climb but your feet slips on a rock and you almost fall, at this point your twenty to twenty-five meters up the cliff… After more climbing you almost see the top! But your exhausted from climbing but you don’t give up and see a little platform to the right of you. You decided to go to the platform to get a rest. When you reach the small platform you sit on it but it starts crumbling and then the platform detaches form the cliff and you start falling to the ground. After a few seconds you fall face first to the ground and die. You died want to start over?")
    choice = input('Yes or No: ')
    if choice in Yes:
        beforewestart()
    elif choice in No:
        print('Goodbye!')
    
def tekst5():
    print("You decided to join Jennifer on her business and then go visit her house. After a little while of walking you see a small house build in to a weird looking tree. You enter the small house while almost bumping your head in the entrance. Jennifer says: Make yourself at home. I don’t get visitors very often so I hope you don’t mind the mess. You don’t mind because your apartment has always been such a mess, you notice something in the corner of the room… It look like some bones from a creature, after inspecting the bones a little bit more you see that they are human bones! You were surprised and started to doubt what Jennifer’s goal is with you. You want to leave as soon as possible, so you ask Jennifer where is a good place to setup a base camp. Jennifer knows a good place to set up a camp and she responds with telling you to go to the west because to the east there are a lot of mountains to climb and that is not useful while travelling. Do you go west (yes) or east (no)?")
    choice = input('Yes or No:')
    if choice in Yes:
        tekst6()
    elif choice in No:
        tekst3()
    
def tekst6():
    print('You decided to go east to setup a camp and also so you can explore more of the lands without having to build a camp afterwards. After ten minutes of walking you spot a open spot in the woods but it is still well hidden. Do you make your camp in the hidden spot Yes or No?')
    choice = input('Yes or No: ')
    if choice in Yes:
        tekst7()
    elif choice in No:
        print("DEAD END")
        choice2 = input('want to start over yes or no?')
        if choice2 in Yes:
            beforewestart()
        elif choice2 in No:
            print('Goodbye!')
    
def tekst7():
    print("You decided to walk further down the path to maybe find a better spot. After even more walking you enter a open field. You make your small camp and you decide to go find some food, you find some weird looking berry’s but you choose to eat because you are very hungry and thirsty. After you found a river and drank something you feel a lot better and you head back to the camp. You come back to your camp and you think what you should do next, are you going to stay up for longer or are you going to sleep. Do  you go to bed (yes) or stay up (no)? ")
    choice = input('Yes or No: ')
    if choice in Yes:
        tekst8()
    elif choice in No:
        tekst9()

def tekst8():
    print("You go to sleep. After what you think are a few hours you hear some rumbling in the bushes. You get out of your makeshift hut and look around, you don’t see anything at first but you see a tiny hat pointing above the bushes. Do you shout at the thing in the bushes or do you hide somewhere else. Do you shout (yes) or hide (no)?")
    choice = input('Yes or No: ')
    if choice in Yes:
        badending1()
    elif choice in No:
        goodending1()
    
def tekst9():
    print(' Your not sleepy enough to sleep so you stay up for a little longer. When you are still awake you make a sharp stick, because you had nothing else to do. You start to get sleepy and fall asleep in your hut. Sometime later you wake up because you thought you heard something and you see a figurine standing outside your hut! Do you call out to the figurine or fight it with your stick? Do you fight (yes) or call out to (no)?')
    choice = input('Yes or No: ')
    if choice in Yes:
        neutralending1()
    elif choice in No:
        goodending1()
    
def badending1():
    print("You sleep and sleep until you feel a itching pain in your back, you were bitten by Jennifer! You feel your head getting lighter and lighter, just then you see Jennifer walking up towards you… She ask you to die already she hasn't had dinner in two weeks, you feel your body getting weaker and weaker until you die never to be seen again…")
    choice = input('Want to play again? Yes or No: ')
    if choice in Yes:
        beforewestart()
    elif choice in No:
        print('Goodbye!')
    
def neutralending1():
    print('You decide to fight what is outside your tent and when you storm out with the stick in your hand you see two armored man with guns and a flashlight standing right in front of you. In the adrenaline that is flowing through you, you attack the man. Before you can even reach the man you are knocked out by the handle of the gun, when you wake up you see yourself lying in a lab.. ')
    choice = input('Want to play again? Yes or No: ')
    if choice in Yes:
            beforewestart()
    elif choice in No:
        print('Goodbye!')
    
def goodending1():
    print("You call out to the thing outside your tent with hello and are you friendly. The thing responds with: ‘Yes we are, are you weaponed come out with you hands in the air!’ You doubt them for a second but you go outside anyways because maybe they can help you? You get outside and you see two armored man with guns and a flashlight standing right in front of you. You are so happy to see people after such a long time and ask them if they know a way out of this place, the men know a way out so they bring you to a elevator that sends you in to a lab of some sorts where there are multiple scientist waiting for you to ask some questions. After a few days you are brought home and fall right asleep on the couch.")
    choice = input('Want to play again? Yes or No: ')
    if choice in Yes:
        beforewestart()
    elif choice in No:
        print('Goodbye!')
    
def tekst10():
    print('hi')

    