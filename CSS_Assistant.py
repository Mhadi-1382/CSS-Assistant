
# CSS Assistant v1.0 (Support CSS3) - 35 Command CSS and 6 Command System
# Built by Mahdi Rabiee
# Created: Sunday, June 6, 2022


import speech_recognition as sr
from colorama import Fore
import platform
import pyttsx3
import random
import os


""" Configure Speaking """
Engine = pyttsx3.init('sapi5')
Engine.setProperty('rate', 140)
Voices = Engine.getProperty('voices')
Engine.setProperty('voice', Voices[0].id)

def speak(text):
    Engine.say(text)
    Engine.runAndWait()


""" Get User """
PlatFormUserName = platform.uname()
GetUser = PlatFormUserName.node


""" Clear Screen """
os.system("cls")


""" Splash Screen """
SplashScreen = """ 

    | C S S  A S S I S T A N T
    | ------------------------

 """
print(Fore.CYAN + SplashScreen + Fore.WHITE)

""" Splash Screen Message """
print("Waiting...")
speak("Hi {0}, Welcome to the CSS Assistant".format(GetUser))


""" Again Clear Screen """
os.system("cls")


""" Again Splash Screen """
print(Fore.CYAN + SplashScreen + Fore.WHITE)


""" Take Commands """
def TakeCommands():
    speak("Please tell me your desired feature")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en')
        print(f"YOU SAID: {query}\n")
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""
    except sr.RequestError:
        speak("Check your connection.")
        return ""
    except:
        speak("Please try again.")
        return ""
        
    return query

    # query = input("TYPE: ")
    # return query


""" CSS Commands """
while True:

    query = TakeCommands().lower()


    if 'add class' in query:
        speak("Adding your class")
        ClassInp = input("\nClass name (Sample: .class or class): ")
        ClassElement = " {\n"
        Tag = "{0}{1}".format(ClassInp, ClassElement)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
    elif 'end class' in query:
        speak("End class")
        Tag = "}\n"
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()

    elif 'add id' in query:
        speak("Adding your id")
        IDChar = "#"
        IDInp = input(f"\nID name: {IDChar}")
        IDElement = " {\n"
        Tag = "{0}{1}{2}".format(IDChar, IDInp, IDElement)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
    elif 'end id' in query:
        speak("End id")
        Tag = "}\n"
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()

    elif 'comment' in query:
        speak("Adding your comment")
        CommentInp = input("\nYour comment: ")
        Tag = "/* {0} */\n".format(CommentInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Comment added.")

    elif 'color' in query:
        speak("Adding your color")
        ColorInp = input("\nColor: ")
        Tag = "\tcolor: {0};\n".format(ColorInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Color added.")

    elif 'width' in query:
        speak("Adding your width")
        WidthInp = input("\nWidth: ")
        Tag = "\twidth: {0};\n".format(WidthInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Width added.")

    elif 'height' in query:
        speak("Adding your height")
        HeightInp = input("\nHeight: ")
        Tag = "\theight: {0};\n".format(HeightInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Height added.")

    elif 'margin' in query:
        speak("Adding your margin")
        MarginInp = input("\nMargin: ")
        Tag = "\tmargin: {0};\n".format(MarginInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Margin added.")
    
    elif 'padding' in query:
        speak("Adding your padding")
        PaddingInp = input("\nPadding: ")
        Tag = "\tpadding: {0};\n".format(PaddingInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Padding added.")

    elif 'font-size' in query:
        speak("Adding your font-size")
        FontsizeInp = input("\nFont-size: ")
        Tag = "\tfont-size: {0};\n".format(FontsizeInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Font-size added.")

    elif 'font-family' in query:
        speak("Adding your font-family")
        FontfamilyInp = input("\nFont-family: ")
        Tag = "\tfont-family: {0};\n".format(FontfamilyInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Font-family added.")

    elif 'font-weight' in query:
        speak("Adding your font-weight")
        FontweightInp = input("\nFont-weight: ")
        Tag = "\tfont-weight: {0};\n".format(FontweightInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Font-weight added.")

    elif 'font-style' in query:
        speak("Adding your font-style")
        FontstyleInp = input("\nFont-style: ")
        Tag = "\tfont-style: {0};\n".format(FontstyleInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Font-style added.")

    elif 'text-align' in query:
        speak("Adding your text-align")
        TextalignInp = input("\nText-align: ")
        Tag = "\ttext-align: {0};\n".format(TextalignInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Text-align added.")

    elif 'text-decoration' in query:
        speak("Adding your text-decoration")
        TextdecorationInp = input("\nText-decoration: ")
        Tag = "\ttext-decoration: {0};\n".format(TextdecorationInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Text-decoration added.")

    elif 'direction' in query:
        speak("Adding your direction")
        DirectionInp = input("\nDirection: ")
        Tag = "\tdirection: {0};\n".format(DirectionInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Direction added.")

    elif 'background' in query:
        speak("Adding your background")
        BackgroundInp = input("\nBackground: ")
        Tag = "\tbackground: {0};\n".format(BackgroundInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Background added.")

    elif 'list-style' in query:
        speak("Adding your list-style")
        ListstyleInp = input("\nList-style: ")
        Tag = "\tlist-style: {0};\n".format(ListstyleInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("List-style added.")

    elif 'opacity' in query:
        speak("Adding your opacity")
        OpacityInp = input("\nOpacity: ")
        Tag = "\topacity: {0};\n".format(OpacityInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Opacity added.")

    elif 'border' in query:
        speak("Adding your border")
        BorderInp = input("\nBorder: ")
        Tag = "\tborder: {0};\n".format(BorderInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Border added.")

    elif 'radius' in query:
        speak("Adding your border-radius")
        BorderradiusInp = input("\nBorder-radius: ")
        Tag = "\tborder-radius: {0};\n".format(BorderradiusInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Border-radius added.")

    elif 'outline' in query:
        speak("Adding your outline")
        OutlineInp = input("\nOutline: ")
        Tag = "\toutline: {0};\n".format(OutlineInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Outline added.")

    elif 'display' in query:
        speak("Adding your display")
        DisplayInp = input("\nDisplay: ")
        Tag = "\tdisplay: {0};\n".format(DisplayInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Display added.")

    elif 'visibility' in query:
        speak("Adding your visibility")
        VisibilityInp = input("\nVisibility: ")
        Tag = "\tvisibility: {0};\n".format(VisibilityInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Visibility added.")

    elif 'overflow' in query:
        speak("Adding your overflow")
        OverflowInp = input("\nOverflow: ")
        Tag = "\toverflow: {0};\n".format(OverflowInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Overflow added.")

    elif 'position' in query:
        speak("Adding your position")
        PositionInp = input("\nPosition: ")
        Tag = "\tposition: {0};\n".format(PositionInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Position added.")

    elif 'float' in query:
        speak("Adding your float")
        FloatInp = input("\nFloat: ")
        Tag = "\tfloat: {0};\n".format(FloatInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Float added.")

    elif 'box-sizing' in query:
        speak("Adding your box-sizing")
        BoxsizingInp = input("\nBox-sizing: ")
        Tag = "\tbox-sizing: {0};\n".format(BoxsizingInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Box-sizing added.")

    elif 'transform' in query:
        speak("Adding your transform")
        TransformInp = input("\nTransform: ")
        Tag = "\ttransform: {0};\n".format(TransformInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Transform added.")

    elif 'cursor' in query:
        speak("Adding your cursor")
        CursorInp = input("\nCursor: ")
        Tag = "\tcursor: {0};\n".format(CursorInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Cursor added.")

    elif 'z-index' in query:
        speak("Adding your z-index")
        ZindexInp = input("\nZ-index: ")
        Tag = "\tz-index: {0};\n".format(ZindexInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Z-index added.")

    elif 'box-shadow' in query:
        speak("Adding your box-shadow")
        BoxshadowInp = input("\nBox-shadow: ")
        Tag = "\tbox-shadow: {0};\n".format(BoxshadowInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Box-shadow added.")

    elif 'content' in query:
        speak("Adding your content")
        ContentInp = input("\nContent: ")
        Tag = "\tcontent: {0};\n".format(ContentInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Content added.")

    elif 'transition' in query:
        speak("Adding your transition")
        TransitionInp = input("\nTransition: ")
        Tag = "\ttransition: {0};\n".format(TransitionInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Transition added.")

    elif 'animation' in query:
        speak("Adding your animation")
        AnimationInp = input("\nAnimation: ")
        Tag = "\tanimation: {0};\n".format(AnimationInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Animation added.")

    # CSS: FLEXBOX
    elif 'flex' in query:
        speak("Adding your flex")
        FlexInp = input("\nFlex: ")
        Tag = "\tflex: {0};\n".format(FlexInp)
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
        speak("Flex added.")


    elif 'tab' in query:
        speak("Tab")
        Tag = "\t"
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
    elif 'enter' in query:
        speak("Enter")
        Tag = "\n"
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()
    elif 'space' in query:
        speak("Space")
        Tag = " "
        with open("style.css", "a") as file:
            file.write(Tag)
            file.close()

    elif 'clear code css' in query:
        speak("Clear code css")
        ClearCodeCss = '' 
        with open("style.css", "w") as file:
            file.write(ClearCodeCss)
            file.close()
    
    elif 'clear screen' in query:
        speak("Clear screen")
        """ Again Clear Screen """
        os.system("cls")

    elif 'stop' in query:
        speak("Stop CSS Assistant, Goodbye.")
        break

    else:
        ListError = ['This command is not allowed.', "Sorry, I didn't understand."]
        ListErrorRandom = random.choice(ListError)
        print(Fore.YELLOW + ListErrorRandom + Fore.WHITE)
        speak(ListErrorRandom)