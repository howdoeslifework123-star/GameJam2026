define m = Character("Mariana", color="#47dd4e")
define l = Character("Lunacello", color="#e68302")
define w = Character("Wyatt", color="#e8d905")
define j = Character("Jecyka", color= "#c40303")
define c = Character("Cillstead", color= "#0b0b9f")
define cc = Character("Sarah", color= "#0b0b9f")
define u = Character("Unrevealed", color="#605732")
# Normal happy, sad, angry, shocked ^

define host = Character("Sir Veridan, The Altruist", color="#0f4500")
define pov = Character("[povname]", color="#d3d3d3")
define lore = Character("Creed", color="#c8c8c8")

default mari_talk = False
default luna_talk = False
default wyatt_talk = False 
default jecyka_talk = False 
default cill_talk = False 

default sus = 1
default unsus = 1

default overall_talk = 0

image davidend = Movie(play="David.webm",size=(1920,1080),loop=False)

image neonend = Movie(play="neon.webm",size=(1920,1080),loop=False)

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
 

transform half_size:
        zoom 0.5

label start:
    scene bg black
    with fade
    pause 2
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
    $ povname = povname.capitalize()

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

        scene bg black
        pause 2
        
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
        
        scene bg black
        pause 2

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
        
        scene bg black
        pause 2

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
        
        scene bg black
        pause 2

        $ renpy.music.set_volume(0.3, delay=0, channel='movie')
        call screen escape_only_movie("images/movies/david.webm")

        return

elif povname == "Sarah":
        hide host normal
        show host happy
        with fade
        "I don't want to forget her..."

        "I don't want to forget..{w} any of them."

        pov "\'[povname]\'.. You may call me \'[povname]\'"

        "So I'll use her name..."

        u "Sounds very specific,{w} do you mind me asking,{w} why that name?"

        u "Someone.. special to you perhaps?"

        pov "..."

        pov "No.. It's just a name."

        hide host happy
        show host normal
        with fade

        u "Oh dear guest...{w} names can never be JUST a name.."

        stop music fadeout 2.0
        play music "End Credits Music  Cyberpunk 2077.mp3" volume 0.32
        scene bg black
        pause 5

        scene bg bar
        with fade

        show c normal
        with dissolve

        cc "Dragging me all the way out here won't change my mind, Creed."

        cc "The Crew is dead{w} and a whole damn Organization is about to expose us and wipe our goddamn memory.."

        cc "I'm doing this.."

        lore "I'm done trying to change your mind,{w} Sarah..{w} but you have to let me handle this properly, please!"

        cc "I already let you handle things your way..{w} you have to realize that there is no other way...{w} it's either this, or we both forget each other."

        hide c normal
        show c closed
        with dissolve

        cc "I'd rather have you be the one to remember..{w} I have a bad memory as is , and the Organization hasn't even caught me yet."

        lore "This isn't fair, Sarah..{w} you can't just sacrifice yourself for my sake..{w} I do my own choices!"

        hide c closed
        show c normal
        with dissolve

        cc "Let's make something clear, you idiot..{w} No one's doing any sacrificing in this situation..{w}"

        cc "I'M{w} taking the fall, so they don't target you and vaporize your memories,{w} so you can find me again,{w} and make me remember!"

        lore "Make you remember?! How the hell do you think I'm supposed to make you remember?!"

        cc "I don't know,{w} dancing in heels maybe..{w} Do literally anything in front of me or something."

        cc "Just find me and come talk to me."

        lore "You make it sound like that alone is enough to cure a memory wipe.."

        hide c normal
        show c closed
        with dissolve

        cc "You idiot..{w} you have no idea how memorable your face is."

        lore "What's that supposed to mean?"

        hide c closed
        show c normal
        with dissolve

        cc "When you love someone,{w} can you still see their face when you close your eyes?"

        lore "Yes,{w} of course."

        cc "How 'bout when a blind person falls in love? Do you think they need to picture a face to feel it?"

        lore "No,{w} I don't think so."

        cc "I know it might not seem all too similar,{w} but maybe a memory vaporization is just taking someone's sight."

        cc "You'll lose the ability to see the things you used to see...{w} but they're still there..{w} you'll be able to feel it."

        cc "I might lose sight of you entirely,{w} but you'll still be here,{w} and you'll still see me,{w} and I'll still be able to feel you, because you won't have forgotten me."

        cc "As long as come find me, I'll know you..{w} I'm sure of it."

        lore "...Look,{w} you can't just chalk all of this up into \'feeling\' and other shit."

        lore "We can still run!"

        hide c normal
        show c closed
        with dissolve

        cc "...You don't even believe that shit yourself."

        hide c closed
        show c normal
        with dissolve

        cc "You know how powerful they are.."

        lore "Why can't you be the one to remember instead??"

        cc "They're closer to exposing me than you.."

        cc "Look...{w} just find me,{w} okay?"

        cc "I promise I'll remember.."

        hide c normal
        show c closed
        with dissolve

        cc "If it helps,{w} name yourself Sarah..{w} Maybe I'll find it cute knowing a big grown dude had his parents name him Sarah."

        hide c closed
        show c normal
        with dissolve

        cc "Don't forget them, Creed..{w} Don't forget any of us..."

        cc "Don't forget me.."

        hide c normal 
        with dissolve

        pause 2

        stop music fadeout 2.0
        play music "NocturneCB.mp3" volume 0.3
        scene bg black
        with fade
        pause 3

        hide bg black
        show bg stretch
        with fade

        show host normal
        with dissolve

        u "Ah, is everything alright, [povname]? It seems like you dozed off into a flashback of some sort."

        pov "It's nothing.."

        hide host normal
        show host happy
        with dissolve

        u "Ah, yes...{w} good'ole nothing."

        u "People can never just be \'nothing\', [povname].{w} They deserve a place in your memory.."

        pause 2

        stop music fadeout 2.0
        scene bg black
        with fade
        pause 2

        $ renpy.music.set_volume(0.3, delay=0, channel='movie')
        call screen escape_only_movie("images/movies/neon.webm")

        play music "NocturneCB.mp3" volume 0.3
        show bg stretch
        with fade
        call unsus_increased

        pause 2

        show host normal
        with dissolve

        u "Anyhoo.."

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


        jump menu_ab

        
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
    jump menu_ab

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
    jump menu_ab

label menu_ab:
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
    play music "Cyberpunk 2077 soundtrack - Nocturne Op. 55 No. 1 (Chopin).mp3" volume 0.32
    "You were led to a room, where it's door is just as identical as the few hundreds more of it's same design back in the hall."

    "You think to yourself of how simple as a hall of doors sounds as a foundation for caution is...{w} yet how simultaneously effective it is."

    "Your eyes took some time to get used to the darkness of the room.."

    host "[povname]..."

    host "Welcome!"

    "Your eyes finally adjust.."

    hide bg black
    show bg tablemeet
    with fade

    host "To the Altruist Playground!"

    jump quit
    






label quit: 
    play music "images/Cyberpunk x Vicetone - Never Fade Away (Vicetone Remix).mp3" volume 0.4
    scene bg demo
    pause 180









    return
