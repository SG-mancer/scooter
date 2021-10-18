# Scooter
# A Renpy game written by Shane George (https://github.com/SG-mancer) (c) 2021


# Characters
define p = Character("Ezra", color="#236AB9") #p for player or pillion
define r = Character("Cleo", color="#D61A46") #r for rider (her eyes #342E09)
# the bike color is: #FDDC22

# Characters with no sprites
define x = Character("Wallace") #friend of p
define y = Character("Pat") #friend of p
define j = Character("Delilah") #little sister of p #hikimori she has been in her room for almost a year.
define k = Character("Joleen") #other little sister of p
define l = Character("Eli") #little brother of p


label start:

    # story points
    $ perv = 0 # count pervert
    $ nice = 0 # count cute/nice events
    $ fib = 0 # count lies you have told

    # tracking actions
    $ hold = 0 # Where p holds the rider(0: waist light, 1: hips, 2:waist tight, 3: pockets, 4: hips tight, 5: tighs, 6: breasts)


    call party # party is dead and you are offered a ride into town
    call roman # small talk, about Roman Holiday
    call breeze 

    call history # Shared same class - recall swimming or being only guy/girl in some classes
    call breeze 
    call wind

    call future # As you notice you are lost, you chat about the future...
    call wind # maybe use another puzzle after the future ???

    call present # debrief - depending on your perv, nice and fib points you get different endings

    # ENDING:
    hide bg road
    "GAME OVER\n...\nYou had a score of:\n[perv] Perv points. [nice] Nice points, and told [fib] fibs."
    return


label party:
    # The party is dead, and everyone is going home. Until Cleo offered a lift, it looked like you were going to walk home.
    r "[p], I have a spare helmet."
    "You had started to worry. Your friends [x] and [y] had went home in his Dad's ute, and no-one you asked had a spare seat for a lift into town."
    "It was looking like you would be walking home through the wetlands."
    "The fire was put out, and the party was quickly emptying."
    "It reminded you that it was still too early in the summer to be wearing a short sleeve shirt this late in the evening."
    r "[p], did you want a ride into town with me on my scooter?"
    p "Sure."
    p "I mean thank you. I was starting to think I would have to walk back."
    r "You know we are almost twenty kilometers out of town right? That is half a marathon."
    p "I have no other plans for the night."
    r "Well put on this helmet. Then slide on behind me."

    show scooter smile
    "You {b}nervously{/b} pull on the helmet and then slide onto the scooter behind [r]."
    r "Have you ever riden on the back of a scooter before?"
    menu:
        "Have you ridden on the back of a scooter before?"
        "No":
            p "No, I've never riden pillion before, not even on a push bike."
            r "Don't worry. Relax."
            r "Try and keep still, because if you move around it makes the scooter unballanced."
            r "Hold on. I'm not going to do anthything crazy, but if you want me to stop just tap on my helmet."
            p "Understood, hold on and don't move about."
            $ nice += 1
        "(Lie) Yes, {i}all the time{/i}":
            $ fib += 1
            p "Yeah, all the time. My uncle had a Ducatti..."
            r "Ok. Well try not to fall off."

    scene bg road
    show scooter smile
    "[r] starts up the engine, and slowly gets started."
    menu:
        "Where should you hold?"
        "Back of the seat":
            $ nice += 1
            "You stretch your fingers and grip around the end of the seat as the scooter bounces onto the road."
            r "[p], you should probably move forward a little bit. Don't be shy about holding on around my waist."
            p "Sorry [r]. I didn't want to seem like a perv."
            r "Ha Ha Ha"
            "You move forward on the seat and rest your hands on [r]'s waist."
        "[r]'s waist":
            "You put your hands onto [r]'s waist as the scooter starts moving onto the road."
        "[r]'s hips":
            $ perv += 1
            $ hold = 4
            "As the scooter increases speed, you move forward and grab [r]'s hips."

        
    return


label roman:
    # our characters start talking on the back of the scooter - about Roman Holiday (a movie with a Vespa scooter)
    p "Have you seen Roman Holiday?"
    r "The Audrey Hepburn movie?"
    p "Yes."
    p "In Roman Holiday there is a scene where Gregory Peck rides behind Audrey Hepburn on the vespa."
    r "You think this is like that?"
    if fib == 0:
        p "No. Unless you are saying I look like Gregory Peck."
        r "Are you saying I look like Audrey Hepburn?"
        p "Maybe..."
    else:
        p "Sure..."
        p "But actually I wanted to know if you've seen the movie?"
        r "Because if I say I haven't you will make up some lie, and if I say I have you will say I am like Princess Ann?"
        p "Probabably..."
    
    r "Since we are talking. [p], do you want to chat about school?"
    p "School?\nLike our plans now since graduation was yesterday?"
    r "Yesterday?"
    p "Yeah, it is past middnight now..."
    r "Oh.\nBut I mean talk about school. Do you remember when we were in the same class?"
    return


label history:
    # our characters talk about school
    p "What classes did we use to have together?"
    r "Back in Year 8 and 9 we had all the same classes.\nDon't you rememeber [p]?"
    p "I vaguely remember"
    r "What do you remember about me?"

    menu:
        "What will you tell [r] you remember from 3 years ago?"
        "At the Year 9 camp, you swam out to the rock in the dam":
            call swimming
        "You were the only girl in Technical Drawing and Electronics classes":
            call onlyone
    return


label swimming:
    # chat about swimming, bring up how [p] is a poor swimmer
    p "I remember at the Year 9 camp you didn't fall into the dam when canoeing."
    p "But afterwards you swam out to the rocky island in the middle."
    r "You remember that?"

    menu:
        "Why do you remember [r] swimming that day?"
        "[r] looked to be having so much fun":
            p "I was a little jealous."
            r "Jealous? Why? That water was so cold."
            p "I was too worried about joining in. Because I can't swim..."
            r "You can swim."
        "[r]'s nipples poked through her wet shirt":
            $ perv += 1
            p "Your nipples were visible through your wet shirt that day."
            r "Probably. That mountain water was cold. I remember screaming because the water was too cold."
            ""
            r "[p] do you know what my first memory of you is?"
            p "..."
        
    show scooter smile
    r "I remember in year 8 you swam in the carnival."
    r "You almost came first in your heat and then stopped about a body length short of finishing. I thought you chose to give up, rather than swim in the final."
    p "I didn't know I was coming first. I stopped because I couldn't go on any more."
    p "That day was the furthest I've ever swam...\nActually I haven't even tried to swim a lap of a pool since."
    show scooter surprise
    r "You have never swam a whole lap of a pool?"
    menu:
        "I'm a bit scared of swimming":
            p "I'm not a good swimmer. I get scared when swimming, so I just try to avoid it."
            $ nice += 1
            r "Is that why you skipped lots of PE days?"
            p "Um... I guess so.\nI did avoided school on swimming days."
            r "You should occasionally push yourself...\nYou know, hard work makes us stronger and more interesting."
            p "I guess always avoiding things, also make it more likely you will contemplate the {i}what ifs of chances you didn't take{/i}..."
            r "True..."
            ""
        "I'm a bit concious about my hair and pimples":
            p "I don't like swimming because of my pimples and hairy legs. I think everyone is staring at me."
            r "Your legs are the hairiest I've seen.\nBut you shouldn't worry, no one really takes notice."
            p "I guess it could be worse."
            r "Sure, you could be from Tasmania and have two heads."
            ""

    # If perfect Nice score, you get to see other option at history
    if nice == 4:
        p "Is not avoiding things why you chose Electronics and Drawing in year 9?"
        call onlyone
    return


label onlyone:
    # chat about being the only girl in a class. [r] was only girl in two classes in Year 8 and 9. [p] was only guy in two classes in 11 and 12.
    p "I remember you were the only girl in both Electronics and Technical Drawing."
    r "Oh, I remember that too. I couldn't get any of the other girls to choose those subjects."
    p "Did you like being the only girl in the class?"
    r "What do you think it was like?"
    p "I sort of know.\nIn Year 11 and 12 I was the only boy in my Mathematics and History class."

    menu:
        "How do you feel it is being the only guy in a class?"
        "Strange.":
            p "Being the only guy was strange. There was something different but I can't articulate it."
            p "I think being the only guy in class helped me keep focused."
            r "Focused? You weren't all horny when alone and surrounded by young women?"
            menu:
                "Not at all":
                    $ nice += 1
                    p "Honestly, no.\nDid you get distracted being the only woman in a class full of guys?"
                    r "I didn't really think about it. Those classes were difficult and I struggled in them."
                    p "Oh, I was the opposite.\nI think I was able to study better in History and Mathematics where I was the only guy in class."
                "(Lie) Of course, I had my pick of so many women.":
                    $ fib += 1
                    p "It seemed good on paper. People would assume I had so many women to get close to."
                    p "But with all my pimples and that... you know... {i}nothing happened.{/i}"
                    p "Honestly though, I did better in the classes I was the only guy in."
        "A little bit Lonely.":
            p "Being the only guy was a litte lonely. Sometimes I wished there was someone to gossip to."
            p "Though in my Software and Engineering Studies classes there were no girls."
            r "Do you think that ballanced it out, having two classes with only girls and two classes with only guys?"
            p "No. But I think I did better in my classes with no other guys."
            
    r "I actually didn't know you were the only guy in some of your classes."
    ""
    p "You still haven't answered my question.\nDid you like being the only girl in class?"
    r "Looking back..."
    r "I liked it."
    r "But, at the time being the only girl in some classes cause a little bit of friction with friends."
    r "Also, I wasn't a star in my classes (academically) like you sound to have been."

    return


label future:
    # The player and rider are lost
    # they chat about your future plans
    p "How much further do you think it is?"
    r "..."
    r "Um [p], this road looks familar, but I am unsure where we are."
    menu:
        "Are we lost?":
            "You think we may be lost."
        "Did we take a wrong turn somewhere?":
            ""
        "Are you tired?":
            ""


    return


label present:
    # end the game with the present.
    # arriving in town... going separate ways...

    return

label breeze:
    # a breeze pushes across the road, warning [p] to change his grip.
    # This is the warning of the WIND puzzle.
    $ hold0 = hold

    if hold < 2:
        "A gust of wind pushes you away from [r]."
        r "[p], move a bit closer. The scooter is moving around a bit."
    else:
        "The scooter is pushed around in a gust of wind."
        p "Should I hold on tighter?"
        if hold > 3:
            "[r] screws up her face a little."
            r "Can you...?"
        else:
            "[r] hunches over into the wind a little more."
            "She probably didn't hear your question."
    
    call choosegrip

    # Warn [p] if you are getting creepy where you are holding
    if hold > 3:
        "You think you notice [r] shudder."
        # If this is your first perv act, then offer to adjust grip
        if perv <= 1:
            "{i}Maybe you should try not to grope [r]...{/i}"
            $ hold = hold0
            call choosegrip
    return


label choosegrip:
    # [p] choose a grip to hold onto [r]
    # This is the action in the WIND puzzle
    if hold == 0 or hold == 2:
        "{i}You are currently holding onto [r]'s waist.{/i}"
    elif hold == 1 or hold == 4:
        "{i}You are currently holding onto [r]'s hips.{/i}"
    elif hold == 3:
        "{i}You are currently hugging [r]'s waist.{/i}"
    elif hold == 5:
        "{i}You are currently groping [r]'s tighs.{/i}"
    else:
        "{i}You are currently groping [r]'s breasts.{/i}"
    
    menu:
        "Where should you hold [r]?"
        "hold onto her waist":
            $ nice += 1
            $ hold = 2
            "You hold onto [r]'s sides a little tighter."
        "hug around her waist":
            $ hold = 3
            "You reach around [r]'s waist and hug her."
        "hold around her hips":
            if hold == 4:
                $ perv += 1
                "You grip a little tigher onto [r]'s hips, wondering how many other guys have held her here."
            else:
                $ perv += 1
                $ hold = 4
                "You grip onto [r]'s hips, noticing the seam of her underwear under her dress."
        "hold her inner thighs":
            if hold == 5 or hold == 4:
                $perv += 2
                $ hold = 5
                "You slide your hands towards the middle of [r]'s things, your fingers stretching to touch her intimately."
            else:
                $ perv += 1
                $ hold = 5
                "You slide your hands around [r]'s thighs."
        "hold onto her breasts":
            if hold == 5 or hold == 6:
                $ perv += 2
                $ hold = 6
                "You squeeze onto [r]'s breasts, trying to calculate how small her bra size is."
            else:
                $ perv += 1
                $ hold = 6
                "You hold onto [r]'s chest, your hands cupping her small breasts."

    return


label wind:
    # A strong wind can push [p] off the scooter.
    # This is the resolution of the WIND puzzle
    "A strong wind pushes the scooter across the road."
    if hold <= 2:
        # ENDING:
        # [p] falls of the bike and dies ;_;
        scene bg road
        with fade
        "The wind pushes you away from [r]."
        "You loose your hold on [r]'s waist and slide off the scooter..."
        "The road bounces under you for a brief moment."
        with fade
        hide bg road
        "GAME OVER\nYou fell of the scooter and died.\nYou had a score of:\n[perv] Perv points. [nice] Nice points, and told [fib] fibs."
        $ renpy.full_restart()
    else:
        "You manage to hold onto [r]."
        r "This is a strong wind."
        "You are affraid you are going to be pushed off the bike."
        menu:
            "Tap on [r]'s helmet":
                # Ask [r] to pull over
                p "[r], pull over. We shouldn't be riding in this."
                r "..."
                "It seems [r] can not hear you."
            "Hug [r]":
                if hold == 3:
                    # hug tighter
                    $ nice += 1
                    p "[r], I'm just holding on tighter so we don't blow away."
                else:
                    # stop groping [r] and hug her
                    $ hold = 3
                    "You slide your arms to [r]'s waist and hug them around her."
            "Wait it out":
                #hold out on the back of the bike
                if hold >= 5:
                    # ENDING:
                    # if [p] is groping [r] he will fall off.
                    "As the wind increases, your hands groping [r] loosen."
                    scene bg road
                    with fade
                    "You groping hands slide off [r]..."
                    "The road bounces under you for a brief moment."
                    with fade
                    hide bg road
                    "GAME OVER\nYou died trying to keep groping [r] during strong winds.\nYou had a score of:\n[perv] Perv points. [nice] Nice points, and told [fib] fibs."
                    $ renpy.full_restart()

        "The wind dies down..."
        r "That was a crazy strong wind. Lucky you managed to hold on."
    return