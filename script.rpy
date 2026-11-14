# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Andy",color="#ea3163ff")
define b = Character("cierra", color="#11d4eaff")
transform big:
    zoom 8 
    nearest True 
    xalign 0.5
    yalign 0.5


image room:
    "r.png"
    xsize 1920
    ysize 1080
    fit "cover"



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play sound "alarm.mp3"

    # These display lines of dialogue.

    a "It's Friday the 13th already..."
    stop sound 

    a "Can't wait to meet Cierra at the resturant!!"

    scene black

    "Andy gets ready to go to the station..." 
    scene road
    a "this is the easiest route to go the station..."
    a "I mean, the station is actually right there.."
    
    
    "STOPPP!!!"
    play sound "crash.mp3" 
    scene carcrash
    "OOPSIE" 
    stop sound 
    

    menu:
        "live again":
            jump lvl2
        

label lvl2:
    scene room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play sound "alarm.mp3"
    a "UGHH what a bad dream!!"
    stop sound 
    a "I'll go with another route this time.."
    "How would u like to go the resturant??"

    menu:
        "go with bridge route":
            scene bridge
            "THE BRIDGE IS SHAKING!!!"
            "THE BRIDGE CRUMBLES"
            scene fall
            play audio"quake.mp3"
            a "OH NOOOOOO...."
            stop audio
            jump lvl3
        "take another long empty route":
            "test"
            jump lvl4

label lvl3: 
    scene room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play sound "alarm.mp3"
    a "AM I IN A LOOP OR SMTH?!!"

    # These display lines of dialogue.
    stop sound 

    a "I'll go with another route this time.."
    "How would u like to go the resturant??"
    menu:
        "Take the long empty route":
            jump lvl4

label lvl4: 
    scene resturant 
    "Andy arrives at the resturant"
    play sound "Resturant.mp3"
    show cierra 
    b "i have been waiting for u for so long..where have u been??"
    a  "hey cierra.. i'm really starving why dont we talk after we decide what to eat?"
    b "sure.. do u crave anything specific..i'll take steak for myself"
    a "i don't know let me see the options"
    menu:
        "puffer fish":
            jump lvl5 
        "steak ":
            jump lvl6
 
label lvl5:
    scene room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play sound "alarm.mp3"
    a "WHY I DO KEEP DYING IN DUMB WAYS!!!"
    stop sound 
    a "I need to figure out how to escape.."
    a "i'll take the long route again.."
    scene resturant 
    "Andy arrives at the resturant"
    play sound "music.mp3"
    scene resturant
    show cierra
    b "i have been waiting for u for so long..where have u been??"
    a  "hey cierra.. i'm really starving why dont we talk after we decide what to eat?"
    b "sure.. do u crave anything specific..i'll take steak for myself"
    a "NOOO PUFFER FISH..i'll take steak for sure"
    stop sound
    menu: 
        "steak":
            jump lvl6


label lvl6:
    scene resturant
    show cierra2
    b "we are talking about wedding prepertaions and your are not even paying attention!!"
    b "IS EVERYTHING OKAYY??!!"
    menu:
        "tell the truths":
            jump lvl7
        "lie to her":
            jump lvl7
            

label lvl7:
    b "Who do u think u are lying to??"
    b "a little girl??"
    b "YOU THINK YOU CAN DUMP ME AFTER ALL OF THIS??"
    play audio "glass.mp3"
    "Anger drove cierra to hit Andy with the glass bottle"
    stop audio 
    menu:
        "hit cierra back":
            jump lvl8
        "Accept your fate":
            jump lvl9 

label lvl8: 
    scene beach
    "CIERRA BLEEDED TILL DEATH..."
    "YOU ARE NOW WANTED..."
    "you live on an island with a fake identity"
    "THE ENDING"
    return
label lvl9:
    scene hell
    "YOU ARE DEAD!!"
    a"WAIT WHAT AM I DOING HERE???"
    a"HEll after all of that??"
    "THE ENDING"

    # These display lines of dialogue.
    # This ends the game.

    return

