
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
    if choice in Yes:
        tekst1()
    elif choice in No:
        tekst10()

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
    print('You chose to avoid the creature because it might be dangerous, you take a turn to get away from the creature and after ten minutes of walking you end up on top of a hill. The view is much better on top of the hill and you see a weird white shaft about 10 kilometers to the north from your position and you see a big building 10 kilometers to the south of your position. Do you go north(Yes) or south(No)?')
    choice = input('Yes or No: ')
    if choice in Yes:
        tekst11()
    if choice in No:
        tekst19()

def tekst11():
    print(' you chose to go to the with shaft because it looks like it is going to the surface. You start your long hike after what feels like two/three hours later are getting very sleepy from al the walking you have done. You see a light source in the distance. Do you go towards the light source Yes or No?')
    choice = input('Yes or No: ')
    if choice in Yes:
        tekst12()
    elif choice in No:
        tekst13_1()

def tekst12():
    print('You are curious about the light source so you go towards it. Some time passes and you see the light moving in a weird way… Do you continue to follow the light Yes or No?')
    choice = input('Yes or No:')
    if choice in Yes:
        neutralending2_1()
    elif choice in No:
        tekst13_2()

def tekst13_1():
    print('You do not trust the light source anymore so you head around the light source. You walk some more and find a nice place to take a rest. You go to sleep. After a nice nap you find yourself in a thick jungle now that you can see around you. You hear some flowing water and you walk towards the sound of the water. You find a river that is flowing towards the white shaft. Do you continue to walk along the river bank (Yes) or not (No)?')
    tekst13_3()

def tekst13_2():
    print('You don’t want to find out who is committing that light source so you walk around the light source. After some more walking you find a river with flowing water so you drink something a go take a nap. You fall asleep. After a nice nap you find yourself in a thick jungle now that you can see around you. The river is flowing toward the white shaft you see in the distance. Do you continue to walk along the river bank (Yes) or not (No)?')
    tekst13_3()

def tekst13_3():
    choice = input('Yes or No: ')
    if choice in Yes:
        tekst14()
    elif choice in No:
        tekst16()

def tekst14():
    print('You go walk along the riverbank because it leads straight to the white shaft after a little while of walking you reach a lake! You observe the lake to see if there is a way around the lake, but you see a small boat. Do you take the boat (Yes) or walk around the lake (No)?')
    choice = input('Yes or No: ')
    if choice in Yes:
        tekst15()
    elif choice in No:
        tekst16()


def tekst15():
    print('You take the boat because that is faster in every way. You step into the boat it is a little bit small but you can make do, you see two paddles. You grab the paddles and start rowing to get to the other side. When you reach the middle of the lake you see a shadow in the water. Suddenly a black tenacle comes out of the water and grabs you! The tentacle drags you underwater and you try to break free but you can’t. After a few minutes everything goes dark… You died want to start over? ')
    choice = input('Yes or No: ')
    if choice in Yes:
        beforewestart()
    elif choice in No:
        print('Goodbye!')

def tekst16():
    print('You go away from the river because you think their could be dangerous creatures near the riverbank, but you keep close to river it is your compass to the white shaft thing. After a little while of walking you see the river expanding and you see a small lake instead of the river you continue walking along side the river but something catches your eyes. A beautiful flower growing next to the lake. Do you get the flower Yes or No?')
    choice = input('Yes or No: ')
    if choice in Yes:
        tekst18()
    elif choice in No:
        tekst17()

def tekst17():
    print('You don’t get the flower because you think to yourself the their still could be danger in the water. You continue to walk to the white shaft. Some time later you reach the bottom of the white tower. You see two men with weapons and two woman with white lab coats on. Do you approach the men yes or no? ')
    goodending2_1()

def tekst18():
    print('You are so hypnotized by the flower before you know it you are next to it. You want to grab the flower, but as soon as you come in contact with the flower you fall unconscious. After some time you wakeup in a fully white room with some glass to the left of it and you see two people standing there.  We don’t want to hurt you, we just want to ask some questions the first man said.')
    neutralending2_1()

def tekst19():
    print('You chose to go south because the building looks more interesting than the white shaft. After a little while of walking you see two deformed creatures. You try to avoid them but they spot you somehow? They shout HEY WHO ARE YOU. Do you respond Yes or No?')
    choice = input('Yes or No: ')
    if choice in Yes:
        tekst21_1()
    elif choice in No:
        tekst20()

def tekst20():
    print('You take a run because your scared to talk to the creatures but they start following you and screaming. HEY WE JUST WANT TO TALK. After a little while of running away from them you hide behind some bushes. They are still calling out to you, WE DON’T WANT TO HARM YOU WE JUST WANT TO TALK! Do you risk talking to them or not?')
    choice = input('Yes or No: ')
    if choice in Yes:
        tekst21_2()
    elif choice in No:
        deadend20()

def deadend20():
    print('You are to scared to talk to them so you slowly backup and try to not make a noise, but you don’t look behind you and you fall of a cliff. Luckily you can grab a rock to not fall to your death then you see the two creatures hanging over the cliff edge. Are you okay? One asks before you could even respond to the creature, the stone snaps of the cliff and you came plummeting down to the ground below. You died want to start over?')
    choice = input('Yes or No: ')
    if choice in Yes:
        beforewestart()
    elif choice in No:
        print('Goodbye!')

def tekst21_1():
    print('You take up all your courage to talk to the creatures. You walk up to them and say: Hey who are you? The creatures respond with: I am Derric and my friend here is called Hank. You ask them if they know a way to that big building. Derric responds: Just keep walking that way and you will reach it some time soon! You thank them and continue your journey towards the big building.')
    tekst21_3()

def tekst21_2():
    print('You take up all your courage to talk to the creatures. You walk up to them and say: Hey who are you? The creatures respond wit: o their you are why are you running away from us? Oh our names are Derric and Hank. You respond with: I was scared because I don’t know who I can trust down here, but do you know a way to that big building? Derric responds: Just keep walking towards it and you will be there in no time. You thank them and depart ways with Derrick and Hank.')
    tekst21_3()

def tekst21_3():
    print('You continue to walk towards the building after a short while you see a giant wall with a gate to your left. Do you climb the wall (yes) or walk towards the gate (no)?')
    choice = input('Yes or No: ')
    if choice in Yes:
        badending2()
    elif choice in No:
        goodending2_2()
    
def badending2():
    print('You start to climb the fence but you get electrocuted as soon as you reach the top.. You find yourself in a hospital bed. You ask the person next to you what happened. He tells you that you got electrocuted and paralyzed in your legs so you need to be in a wheelchair for the rest of your life, but you are back in new York. ')
    choice = input('Want to play again? Yes or No: ')
    if choice in Yes:
        beforewestart()
    elif choice in No:
        print('Goodbye!')

def neutralending2_1():
    print('You keep following the lights until you see and squad of armored men. You call out to them and they shoot you! Everything goes dark and you wake up in a hospital. You ask the nurse where you are and she say that you’re in new York. You are so happy because you are back home!')
    choice = input('Want to play again? Yes or No: ')
    if choice in Yes:
        beforewestart()
    elif choice in No:
        print('Goodbye!')
        
def neutralending2_2():
    print('You answer their questions and then they let you out of your cell to inspect you on diseases and bacteria that may be on you. Then they push you out of their building and you need to find your way back home by lifting for rides and stuff. ')
    choice = input('Want to play again? Yes or No: ')
    if choice in Yes:
        beforewestart()
    elif choice in No:
        print('Goodbye!')

def goodending2_1():
    print('You call out to the people and walk out of the bushes. You see the two woman getting scared of your voice and the two men point their gun towards you. You walk closer and the four people are amazed because they have never seen another person down here except scientists and guards. They take you back up to the surface and bring you back home! The end')
    choice = input('Want to play again? Yes or No: ')
    if choice in Yes:
        beforewestart()
    elif choice in No:
        print('Goodbye!')

def goodending2_2():
    print('You walk towards the gate and call out to the guard that is standing there. The guard turns towards you and says: Huh another human that isn’t a scientist, how did you get down here? You tell him your entire story and the guards brings you to his boss who is also surprised but just sends you back to the surface and back home!')
    choice = input('Want to play again? Yes or No: ')
    if choice in Yes:
        beforewestart()
    elif choice in No:
        print('Goodbye!')
