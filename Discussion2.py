define m = Character("Mariana", color="#47dd4e")
define l = Character("Lunacello", color="#e68302")
define w = Character("Wyatt", color="#ffee00")
define j = Character("Jecyka", color= "#ff0000")
define c = Character("Cillstead", color= "#0000ff")
define u = Character("Unrevealed", color="#605732")
define pov = Character("Unrevealed", color="#605732") #remove
define povname = Character("Unrevealed", color="#605732") #remove
# Normal happy, sad, angry, shocked ^

define host = Character("Sir Veridan, The Altruist", color="#0f4500")
define pov = Character("[povname]", color="#000000")

default mari_talk = 0
default luna_talk = 0
default wyatt_talk = 0
default jecyka_talk = 0
default cill_talk = 0

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
#    if sus >= =21:
#       call sus_ending #ending 3(bad)
#    elif sus == 19:
#       call mid_ending #ending 2(mid)

#label compassionate_heart:
#   if unsus >= 21:
#      call unsus_ending #ending 1 (good)
#   elif unsus == 19:
#      call mid_ending #ending 2(mid)

label start:
    jump Discussion_2

label Discussion_2:

    scene bg black
    with fade
    play music "Cyberpunk 2077 soundtrack - Nocturne Op. 55 No. 1 (Chopin).mp3" volume 0.35
    hide bg black
    show bg tablemeet
    with dissolve

    show host normal
    with fade

    "Such heavy questions ended up making you eat a ton.."

    "Like a black hole would, you devour such dinner while barely even chewing.."

    "Your stomach growled, you have no idea if it was asking for more, or if it wanted to kill itself..{w} but a buzzing noise from The Host's phone kept your stomach at bay."

    host "Oop,{w} that's me.."

    hide host normal
    show host happy
    with dissolve

    host "Apologies everyone,{w} but I have to tend to some other matter once more.."

    host "I hope everyone enjoyed dinner for what it was!{w} Kudos to the chef, feel free to thank her at her station.."

    host "Now, if you'll please excuse me..{w} I will return quite shortly after."

    hide host happy
    with fade

    "As The Host heads out once again for the second time,{w} you find yourself yet in another conundrum of choices.."

    "To Converse with the group..{w}"

    "Or to stay hushed..{w}"

    menu:
        "Converse":
            jump converse_2

            return
        "Hush":
            jump hush_2

            return
    
    label converse_2:
        "You decide to chalk up conversations between everyone, in which you first pick-{w}"
        menu:
            "The Conductor":
                jump conductor_2
                return

            "The Scouter":
                jump scouter_2
                return

            "The Agent":
                jump agent_2
                return

            "The Dungeon Master":
                jump master_2
                return

            "The Coach":
                jump coach_2
                return
    

    label conductor_2:
        ""

        return

    label scouter_2:
        ""

        return

    label agent_2:
        ""

        return

    label master_2:
        ""

        return

    label coach_2:
        ""

        return
        

    
    label hush_2:
        "You choose to avoid further interaction with the group,{w} you deem it unnecessary,{w} as if you are trying to determine your mind as a stronghold of conviction agaisnt conversing with cruel people."
        scene bg minute
        with fade
        pause 3
        
        hide bg minute
        show bg tablemeet
        with fade
        
        "Minutes of nothingness and silence..{w} You wonder how a room full of such people could be as peaceful as a field of sheep.."

        "Yet you know damn well that this is no field of sheep,{w} but a den of wolves.."

        "The minutes grew on you,{w} as you still feel the weight of the food from dinnertime.."

        "This smell of the room is strong,{w} most likely from all the perfume of the Conductor,{w} but regardless,{w} the room is heavy."

        "As you wait for the Host's return,{w} you've noticed \'The Agent\' herself staring daggers towards your direction,{w} you lack the thought to comprehend why."

        scene bg minute
        with fade
        pause 3

        show bg tablemeet
        with dissolve

        show host happy
        with dissolve

        "The Host arrives for the second time,{w} with this time, holding a pen and some papers.."

        host "Greetings yet again!{w} This'll sound spontaneous as much,{w} but is anyone here willing to solve a couple equations for me, please?"

        hide host happy
        show host normal
        with dissolve

        host "...Hah, why did I even ask!{w} I know just the right person for such tasks as these.."

        host "[povname], would you please care to spare a bit of your knowledge with us...{w} That is if you don't mind of course." #add povname

        menu:
            "Agree to the Equations (Bonus points)":
                jump equations_event2a
                return

            "Simply ignore the request":
                jump Discussion_2a
                return

    label equations_event2a:
        pov "*Sigh* Sure,{w} why not...{w} give it here."

        hide host normal
        show host happy
        with dissolve

        host "Perfect!"

        host "Here..{w} they are all Limit laws,{w} and as a hint,...{w} because why not."

        hide host happy
        show host Normal
        with dissolve

        stop music fadeout 2.0
        play music "8bitDep.mp3" volume 0.3

        host "They are all limits at infinity."

        pov "...cool"

        scene bg limit1
        with fade
        pause 5

        show bg black
        with fade

        menu:
            "One half":
                call unsus_increased
                jump equations_event2b
                return

            "Infinite":
                jump equations_event2b
                return

    label equations_event2b:
        show bg tablemeet
        with dissolve
        show host normal
        with dissolve

        host "Next!"

        scene bg limit2
        with fade
        pause 5

        show bg black
        with fade

        menu:
            "Three over five":
                jump equations_event2c
                return

            "Infinite":
                call unsus_increased
                jump equations_event2c
                return

    label equations_event2c:
        show bg tablemeet
        with dissolve
        show host normal
        with dissolve

        host "Aaand, lastly."

        scene bg limit3
        with fade
        pause 5

        show bg black
        with fade

        menu:
            "Infinite":
                call unsus_increased
                jump equations_result
                return
            "Five over one":
                jump equations_result
                return

    label equations_result:
        host "Well done!{w} Well..{w} I think."

        host "I'll go check on the answers later.."

        jump Discussion_common


        return




    label Discussion_2a:
        pov "...{w}"

        host "...I guess I will take that as a no."

        host "No worries,{w} I can get someone to solve it later I guess."

        host "Anyhoo..."

        jump Discussion_common

        return


    label Discussion_common:

        return



        

    label quit: 
    stop music fadeout 2.0
    play music "End Credits Music  Cyberpunk 2077.mp3" volume 0.4
    scene bg bloodend with fade
    pause 120
    

    

    return
