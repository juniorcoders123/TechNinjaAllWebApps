import streamlit as st
from random import randint
from gtts import gTTS
from googletrans import Translator

def app():
    insults = [
        "I'd like to roast you, but it looks like God already did.",
        "You look like someone set your face on fire and then put it out with a hammer.",
        "The only thing attracted to you is gravity",
        "You’re not good looking enough to be a model, but you’re not smart enough to be anything else",
        "If you’d like to know what sexual position produces the ugliest babies, you should ask your mother.",
        "Can you speak a little louder? I can’t hear you over the sound of how stupid you are.",
        "Why are you even talking to me? So your self esteem can match your IQ?",
        "I’m not insulting you, I’m describing you.",
        "If you hide your big nose and shut your big mouth, people will think you are attractive and well-spoken.",
        "I guess God’s just making anybody these days.",
        "You're so ugly, when your mom dropped you off at school she got a fine for littering.",
        "Some babies were dropped on their heads but you were clearly thrown at a wall.",
        "They say opposites attract. If that's so, you will meet someone who is good-looking, intelligent, and cultured.",
        "I didn’t hear you. I’m busy ignoring an annoying person.",
        "I don't know what your problem is, but I'll bet it's hard to pronounce.",
        "Please excuse me while I transfer you to someone who speaks Fucktard.",
        "It must take a lot of flexibility to fit your foot in your mouth and your head up your ass at the same time.",
        "I don’t have the time nor the crayons to explain things to you",
        "I’d love to keep chatting with you, but I’d rather have AIDS",
        "I bet you swim with a t shirt on",
        "You have all the charm and charisma of a burning orphanage",
        "Your face is so oily that I’m surprised America hasn’t invaded yet.",
        "If you were any dumber, someone would need to water you twice a week",
        "If you were on fire and I had a cup of my own piss, I’d drink it",
        "Do you still love nature, despite what it did to you?",
        "The thing I dislike most about your face is that I can see it.",
        "If B.S. was music, you’d be an orchestra.",
        "You look like a before picture.",
        "I’ve heard farts more intelligent than you.",
        "You have a perfect face for radio.",
        "They say that a million monkeys on a million typewriters will eventually produce the collected works of Shakespeare. If that theory is correct, I believe you will one day say something intelligent.",
        "If you want to lose ten pounds of ugly fat, may I suggest you start with cutting off your head.",
        "You look like somebody stepped on a goldfish.",
        "I thought the trash got picked up last night, what are you still doing here?",
        "Looking the way you do must save a lot of money on halloween.",
        "I’d love to continue talking with you but my favorite commercial is on tv",
        "I'd love to keep chatting with you, but right now I have to do literally anything else.",
        "Did you get a bowl of soup with that haircut?",
        "If you don’t like what I say about you, it would be a good idea to improve yourself.",
        "Does being that ugly require a license?",
        "You could throw a rock at the ground and miss",
        "There’s no one in this world like you. Or at least I hope so.",
        "You look like a man, and you need to lose some weight.",
        "Did you cancel your barbecue?  Because your grill is messed up",
        "Some people make millions.  You make memes.",
        "Did you forget to wipe or is that your natural scent?",
        "I missed you this week, but my aim is improving.",
        "I'm surprised you've made it this far without being eaten.",
        "Your body looks like your head is inflating a water balloon.",
        "How do you make an idiot wait?",
        "I'd like to roast you, but I'm too busy judging your choices.",
        "You are the worst part of everybody's day.",
        "If your face were scrambled it would improve your looks.",
        "I hope you don't feel the way you look.",
        "In the book of Who's Who, you are listed as What's That?",
        "It's surprising to me that a pig's bladder on a stick has gotten so far in life.",
        "Sorry.  I'm on the toilet and I can only deal with one shit at a time.",
        "If you fell into a river it would be unfortunate, but if anyone pulled you out it would be a disaster.",
        "You are the discount version of whatever celebrity you look like.",
        "When you go to the dentist, he needs anaesthetic.",
        "The fact that you are still alive is evidence that natural disasters are poorly distributed.",
        "You are so dumb you can't fart and chew gum at the same time.",
        "I was going to give you a nasty look, but I see you already have one.",
        "Me think'st thou are a general offence and every man should beat thee.",
        "I don't try to explain myself to idiots like you.  I'm not the Fucktard Whisperer.",
        "Your face invites a slap."
    ]

    praises = [
        "You’re that “Nothing” when people ask me what I’m thinking about.",
        "You look great today.",
        "You’re a smart cookie.",
        "I bet you make babies smile.",
        "You have impeccable manners.",
        "I like your style.",
        "You have the best laugh.",
        "I appreciate you.",
        "You are the most perfect you there is.",
        "Our system of inside jokes is so advanced that only you and I get it. And I like that.",
        "You’re strong.",
        "Your perspective is refreshing.",
        "You’re an awesome friend.",
        "You light up the room.",
        "You deserve a hug right now.",
        "You should be proud of yourself.",
        "You’re more helpful than you realize.",
        "You have a great sense of humor.",
        "You’ve got all the right moves!",
        "Is that your picture next to “charming” in the dictionary?",
        "Your kindness is a balm to all who encounter it.",
        "You’re all that and a super-size bag of chips.",
        "On a scale from 1 to 10, you’re an 11.",
        "You are brave.",
        "You’re even more beautiful on the inside than you are on the outside.",
        "You have the courage of your convictions.",
        "Aside from food. You’re my favorite.",
        "If cartoon bluebirds were real, a bunch of them would be sitting on your shoulders singing right now.",
        "You are making a difference.",
        "You’re like sunshine on a rainy day.",
        "You bring out the best in other people.",
        "Your ability to recall random factoids at just the right time is impressive.",
        "You’re a great listener.",
        "How is it that you always look great, even in sweatpants?",
        "Everything would be better if more people were like you!",
        "I bet you sweat glitter.",
        "You were cool way before hipsters were cool.",
        "That color is perfect on you.",
        "Hanging out with you is always a blast.",
        "You always know — and say — exactly what I need to hear when I need to hear it.",
        "You smell really good.",
        "You may dance like no one’s watching, but everyone’s watching because you’re an amazing dancer!",
        "Being around you makes everything better!",
        "When you say, “I meant to do that,” I totally believe you.",
        "When you’re not afraid to be yourself is when you’re most incredible.",
        "Colors seem brighter when you’re around.",
        "You’re more fun than a ball pit filled with candy. (And seriously, what could be more fun than that?)",
        "That thing you don’t like about yourself is what makes you so interesting.",
        "You’re wonderful.",
        "Everyday is just BLAH when I don’t see you For reals! (awesome – you are halfway through the list. You’re awesome!)",
        "Jokes are funnier when you tell them.",
        "You’re better than a triple-scoop ice cream cone. With sprinkles.",
        "Your hair looks stunning.",
        "You’re one of a kind!",
        "You’re inspiring.",
        "If you were a box of crayons, you’d be the giant name-brand one with the built-in sharpener.",
        "You should be thanked more often. So thank you!!",
        "Our community is better because you’re in it.",
        "Someone is getting through something hard right now because you’ve got their back.",
        "You have the best ideas.",
        "You always know how to find that silver lining.",
        "Everyone gets knocked down sometimes, but you always get back up and keep going.",
        "You’re a candle in the darkness.",
        "You’re a great example to others.",
        "Being around you is like being on a happy little vacation.",
        "You always know just what to say.",
        "You’re always learning new things and trying to better yourself, which is awesome.",
        "If someone based an Internet meme on you, it would have impeccable grammar.",
        "You could survive a Zombie apocalypse."
    ]

    max = len(insults)
    max_1 = len(praises)

    langs = ("English", "French", "Spanish", "Hindi", "Bengali")
    st.header("Junior Coders Insulter & Praiser Bot")
    name = st.text_input("Enter your name")
    langchoose = st.selectbox('Select Language', langs)

    insultbtn = st.button("Insult Me")
    praisebtn = st.button("Praise Me")

    translate = Translator()

    if insultbtn:
        if name == '':
            st.warning("Name cannot be empty")
        else:
            if langchoose == "English":
                langcode = 'en'
            elif langchoose == "Spanish":
                langcode = 'es'
            elif langchoose == "French":
                langcode = 'fr'
            elif langchoose == "Hindi":
                langcode = 'hi'
            if langchoose == "Bengali":
                langcode = 'bn'
            chosen = randint(0, max)
            insultorpr = name + ", " + insults[chosen]
            text = translate.translate(insultorpr, dest=langcode)
            tts = gTTS(text=text.text, lang=langcode)
            tts.save('example.mp3')
            audio_file = open(f"example.mp3", "rb")
            audio_bytes = audio_file.read()
            st.markdown(f"## Insult audio:")
            st.audio(audio_bytes, format="audio/mp3", start_time=0)
            st.markdown(f"## Insult text:")
            st.write(text.text)

    if praisebtn:
        if name == '':
            st.warning("Name cannot be empty")
        else:
            if langchoose == "English":
                langcode = 'en'
            elif langchoose == "Spanish":
                langcode = 'es'
            elif langchoose == "French":
                langcode = 'fr'
            elif langchoose == "Hindi":
                langcode = 'hi'
            if langchoose == "Bengali":
                langcode = 'bn'
            chosen_1 = randint(0, max_1)
            insultorpr = name + ", " + praises[chosen_1]
            text = translate.translate(insultorpr, dest=langcode)
            tts = gTTS(text=text.text, lang=langcode)
            tts.save('example.mp3')
            audio_file = open(f"example.mp3", "rb")
            audio_bytes = audio_file.read()
            st.markdown(f"## Praise audio:")
            st.audio(audio_bytes, format="audio/mp3", start_time=0)
            st.markdown(f"## Praise text:")
            st.write(text.text)

