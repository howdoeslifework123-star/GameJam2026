define m = Character("Mariana", color="#47dd4e")
define l = Character("Lunacello", color="#e68302")
define w = Character("Wyatt", color="#ffee00")
define j = Character("Jecyka", color= "#ff0000")
define c = Character("Cillstead", color= "#0000ff")
define u = Character("Unrevealed", color="#605732")
# Normal happy, sad, angry, shocked ^

define host = Character("Sir Veridan, The Altruist", color="#0f4500")
define pov = Character("[povname]", color="#000000")

default mari_trust = 0
default luna_trust = 0
default wyatt_trust = 0
default jecyka_trust = 0
default cill_trust = 0

default sus = 1
default unsus = 1

image davidend = Movie(play="David.webm",size=(1920,1080),loop=False)

screen escape_only_movie(movie_file):
    modal True 
    add Movie(play=movie_file, loop=False)
    key "K_ESCAPE" action Return()

label sus_increased: # bad
    $ sus += 1
    "Suspicions towards you is increased!"
    return


label unsus_increased: # good
    $ unsus += 1
    "Trust towards you is increased!"
    return

#label savagery_terror:
#    if sus >= 10:
#       call sus_ending #ending 3(bad)
#    elif sus == 9:
#       call mid_ending #ending 2(mid)

#label compassionate_heart:
#   if unsus >= 10:
#      call unsus_ending #ending 1 (good)
#   elif compassion == 9:
#      call mid_ending #ending 2(mid)




label start:
    scene bg black
    with fade
    play music "NocturneCB.mp3" volume 0.3
    u "My my!"

    "A strong and inviting voice reaches out to you in this big stretch of a hallway."
    hide bg black
    show bg stretch
    with fade
    

    show host happy
    with dissolve

    u "Welcome, beloved guest...{w} your arrival brings glad tidings to the Organization."

    "The person behind this thick mask in front of you has you aggravated."

    u "A bit late, yes.. {w} but your presence alone compensates for any sort of tardiness."

    hide host happy
    show host normal
    with fade

    "They should know your name, but thinks it's more plausible to let yourself do your own introductions."

    u "It truly is an honor to meet you.. {w} ehmm.."

    label name:
    $ povname = renpy.input("Please input your preferred \"Undercover Title\" ", length=32)
    $ povname = povname.strip()

if povname == "The Altruist":
    pov "\'[povname]\'.. You may call me \'[povname]\'"
    u "Hah, I'm afraid I can't allow that, my dear guest.. {w} Please, try again."
    jump name
elif povname == "The Scouter":
    pov "\'[povname]\'.. You may call me \'[povname]\'"
    u "Hah, I'm afraid that won't do,{w} try again."
    jump name
elif povname == "The Conductor":
    pov "\'[povname]\'.. You may call me \'[povname]\'"
    u "Ah..{w} I think you are mistaken, perhaps you should try again. "
    jump name
elif povname == "The Dungeon Master":
    pov "\'[povname]\'.. You may call me \'[povname]\'"
    u "I'm afraid I can't let you have that title, my dear guest.."
    jump name
elif povname == "The Coach":
    pov "\'[povname]\'.. You may call me \'[povname]\'"
    u "I don't think you are of such stature to be a coach of any team whatsoever.{w} Please, do try again."
    jump name
elif povname == "The Agent":
    pov "\'[povname]\'.. You may call me \'[povname]\'"
    u "Uhm, I highly doubt such a title is plausible for you, my dear guest..{w} Do try again, plesae."
    jump name

# ending 4 (secret ending)
elif povname == "David":
        hide host normal
        show host shocked
        with fade
        u "Oh...{w} that name... {w} surely not.."

        u "I'm afraid that cannot be a title for any reason whatsoever.."

        pov "Why not? It's my nam-"
        hide host shocked
        show host normal
        with fade
        stop music fadeout 2.0
        u "I'm afraid it matters not in this matter, my dear guest...{w} for such a story cannot be told through mere words..{w} but through a-"
        
        $ renpy.music.set_volume(0.3, delay=0, channel='movie')
        call screen escape_only_movie("images/movies/david.webm")
        return

# ending 4 (secret ending)
elif povname == "david":
        hide host normal
        show host shocked
        with fade
        u "Oh...{w} that name... {w} surely not.."

        u "I'm afraid that cannot be a title for any reason whatsoever.."

        pov "Why not? It's my nam-"
        hide host shocked
        show host normal
        with fade
        stop music fadeout 2.0
        u "I'm afraid it matters not in this matter, my dear guest...{w} for such a story cannot be told through mere words..{w} but through a-"
        
        $ renpy.music.set_volume(0.3, delay=0, channel='movie')
        call screen escape_only_movie("images/movies/david.webm")
        return

# ending 4 (secret ending)
elif povname == "Lucy":
        hide host normal
        show host shocked
        with fade
        u "Oh...{w} that name... {w} surely not.."

        u "I'm afraid that cannot be a title for any reason whatsoever.."

        pov "Why not? It's my nam-"
        hide host shocked
        show host normal
        with fade
        stop music fadeout 2.0
        u "I'm afraid it matters not in this matter, my dear guest...{w} for such a story cannot be told through mere words..{w} but through a-"
        
        $ renpy.music.set_volume(0.3, delay=0, channel='movie')
        call screen escape_only_movie("images/movies/david.webm")
        return

# ending 4 (secret ending)
elif povname == "lucy":
        hide host normal
        show host shocked
        with fade
        u "Oh...{w} that name... {w} surely not.."

        u "I'm afraid that cannot be a title for any reason whatsoever.."

        pov "Why not? It's my nam-"
        hide host shocked
        show host normal
        with fade
        stop music fadeout 2.0
        u "I'm afraid it matters not in this matter, my dear guest...{w} for such a story cannot be told through mere words..{w} but through a-"
        
        $ renpy.music.set_volume(0.3, delay=0, channel='movie')
        call screen escape_only_movie("images/movies/david.webm")

        return

if not povname:
    u "I...{w} Uhhh.. {w} Ummmmmm..."

    u "I'm..{w} I'll be..{w} You can call m-"

    hide host normal
    show host happy
    with fade

    "You stutter your way inside the person's funny bone."

    u "Hah, no need to dwell on such trivial matters, my dear guest.."

    hide host happy
    show host normal 
    with fade

    u "After all, you are one of our dear guest..{w} Therefore, I see no other title befitting you other than such."

    $ pov = "Dear Guest"

    "The mask the individual wears portrudes to the left, but you see them pay no mind whatsoever..{w} as if they value their identity as expendable for such an event."

    pov "Very well..{w}"
    
    hide host normal
    show host happy
    with fade

    u "I am very pleased with your appearance alone, [povname]"

    "You see a hand reach out for you, firm and stern as it asks for your reach."

    u "Such pleasantries does not need to be extended any further{w}, please, allow me to lead you to the \'Meeting Room\'."

    hide host happy
    show host normal
    with dissolve

    u "That is unless you have any concerns so far just from our Introductions?"

    "As notice of concern arises, but it felt more like skepticism and suspicions directed towards you."

    u "You might've not noticed it,{w} but you seem shaky,{w} are you feeling ill?"

    u "Perhaps..{w} You are in no way to continue your agenda with us today?"

else:
    hide host normal
    show host happy
    with fade

    u "Perfect!"

    u "I am very pleased with your appearance alone, [povname]"

    "You see a hand reach out for you, firm and stern as it asks for your reach."

    u "Such pleasantries does not need to be extended any further{w}, please, allow me to lead you to the \'Meeting Room\'."
    
    hide host happy
    show host normal
    with dissolve

    u "That is unless you have any concerns so far just from our Introductions?"

    "As notice of concern arises, but it felt more like skepticism and suspicions directed towards you."

    u "You might've not noticed it,{w} but you seem shaky,{w} are you feeling ill?"

    u "Perhaps..{w} You are in no way to continue your agenda with us today?"


menu:

    "There is no need for you to sharpen your deception around me, host...":
        call sus_increased
        jump bad
    

    "Oh, no need to fret upon the little details.":
        call unsus_increased
        jump nice
        
        


label nice:

    pov "Oh, no need to fret upon the little details."

    pov "I have already put in an appearance..{w} Therefore, I will attend."

    pov "Such an agenda must not be missed, after all.."

    hide host normal
    show host happy
    with fade
    
    "A smile of some sort extrudes out of the thick mask."

    u "Hah, well said [povname]"

    u "Such an agenda must not be missed indeed..."

    hide host happy
    show host normal

    u "This gathering shall be a fruitful one."

    u "Of that, I can promise..{w}"

    jump Meeting

label bad:

    pov "There is no need for you to sharpen your deception around me, host...{w} I have no need for your care nor hospitality.."

    pov "I have already put in an appearance..{w} Therefore, I will attend."

    pov "Such an agenda must not be missed, after all.."

    hide host normal
    show host sad
    with dissolve

    u "I see, pardon my ignorance then, [povname]"

    "A frown of some sort extrudes from the thick mask."

    hide host sad
    show host normal
    with fade

    u "Such an agenda must not be missed indeed..."

    u "I can already tell that this gathering shall be a fruitful one."

    u "Oh without a doubt..{w}"

    jump Meeting


label Meeting:

    hide host normal
    show host happy
    with fade

    u "Pardon my ignorance yet again,{w} for I have just completely forgotten my proper etiquette.."

    u "Allow me to Introduce myself, and this year's trade.."

    host "I am Chicago's very own \'Altruist Host\', but I'd prefer you to keep our relationship as adjacent as possible,{w} so you are free to refer to me as \'Sir Veridan\'."

    host "I'd really prefer us to be close...{w} I really hope you value even the smallest relationships life throws at you.." 

    hide host happy
    show host normal
    with fade

    "The inviting face behind the mask turns dead serious."

    host "This year's trade involves one of humanity's greatest treasures,{w} children..."

    host "Children that are not only of great potential,{w} but enhanced in their physical capacity at birth.."

    host "We had a lot of partners who wanted to participate in this year's trade,{w} so you should feel lucky for being able to sit in this year's table..."

    host "Everyone is sure to enjoy this year's event...{w} All of you will only be seated calmly down your spots, awaiting your values."

    host "Although I might have to look over my agenda's here and there..."

    hide host normal
    show host happy
    with dissolve

    "Yet again, a smile of some sort extrudes from the thick mask,{w} but this time..{w} it seemed forced."

    host "Anyhooo.."

    host "Unfortunately we can no longer lengthen our introductions any further...{w} alas, I enjoy these moments too much..{w}"

    hide host happy
    show host normal
    with fade

    host "Now, come come..{w} It is time we introduce you to your spot,{w} all this chatter must have you tiresome."

    "The Host walks after you, directing you towards the correct door amongst the many in the hall."


    host "I'm assuming that you can understand the caution our Organization have for such an event to take place.." 

    host "I'd like to point out that this year's event is actually way more tame than the usual caution we do."

    "The Host yet again, extrudes a smile from their thick mask, as they look at you."

    host "But don't be afraid, [povname]..{w} This year's event will be the best,{w} that I can guarantee you.."

    host "Nothing will go as unplanned..{w} for the greater good."

    stop music fadeout 2.0

    scene bg black
    play music "Cyberpunk 2077 soundtrack - Nocturne Op. 55 No. 1 (Chopin).mp3" volume 0.22
    "You were led to a room, where it's door is just as identical as the few hundreds more of it's same design back in the hall."

    "You think to yourself of how simple as a hall of doors sounds as a foundation for caution is...{w} yet how simultaneously effective it is."

    "Your eyes took some time to get used to the darkness of the room.."

    host "[povname]..."

    host "Welcome!"

    "Your eyes finally adjust.."

    hide bg black
    show bg tablemeet

    host "To the Altruist Playground!"

    jump Discussion_Scenario1

    return


# Discussion_Scenario1




label quit: 
    scene bg black
    play music "End Credits Music  Cyberpunk 2077.mp3" volume 0.4
    
    "The End"

    return


