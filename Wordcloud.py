#Syed Haider Naqvi
#PA4
#20th October,2020
#This program creates a wordcloud with a default text file, or a text file of the users choice

from string import punctuation
from graphics import *
from random import randrange

def numwordChecker(words_list, number_of_words):

    while len(words_list) < number_of_words:
        number_of_words_checker, number_of_words_checker_label = \
        buttonmaker(Point(10,0),Point(90,15),Point(50,7.5)\
        ,"There are not enough words in this file.\nPlease enter another text" \
        + " file or reduce\n number of required words and click continue again",\
        color_rgb(65,179,247),"black", 15)

        continue_click = clickChecker()
        #Used to get a mouseclick until user clicks continue
        
        number_of_words_checker.undraw()
        number_of_words_checker_label.undraw()
        #Undraws the entry boxes for file name and number of words

        file_name, number_of_words = getInput()

        words_list = wordFrequency(file_name)
        #Used to get the list of most common words from the file

    return  words_list

def getInput():

    file_name = entry_text.getText()
    number_of_words = int(entry_number.getText())
    #Used to get the file name and number of words

    return file_name, number_of_words
    
def clickChecker():

    continue_click = wordcloud.getMouse()
    #Used to wait for a mouseclick before proceeding

    while not(continue_click.getX() >= 40 and continue_click.getX() <= 60 and \
              continue_click.getY() >= 15  and continue_click.getY() <= 25):
        continue_click = wordcloud.getMouse()
    #Used to keep getting a mouselick until the user clicks the continue button

    return continue_click

def byNum(counts):

    return counts[1]
    #Used to sort the list of tuples by number

def wordcloudMaker(list_of_words, number_of_words):

    list_of_used_coordinates = []
    #Used to initalise list of coordinates to prevent overlapping

    output_box = Rectangle(Point(2,15),Point(98,90))
    output_box.setFill(color_rgb(65,179,247))
    output_box.draw(wordcloud)
    #Used to draw wordcloud box

    buttonmaker(Point(35,92),Point(65,98),Point(50,95),"Wordcloud!", \
    color_rgb(65,179,247),"black")
    #Used to draw output box and title

    for i in range(number_of_words):
        
        coordinate = (randrange(10,91,16),randrange(20,81,15))
                      
        while coordinate in list_of_used_coordinates:
            coordinate = (randrange(10,91,16),randrange(20,81,15))
        #Used to get a coorindate and keep getting a coordinate until it gets one not already used by another word

        list_of_used_coordinates.append(coordinate)
        #Appends new coordinate to list of used coordinates
            
        word_in_cloud = Text(Point(coordinate[0],coordinate[1]), list_of_words[i][0] )
        size_constant = ((40 * (list_of_words[i][1] - list_of_words[number_of_words - 1][1]))) / \
        (list_of_words[0][1] - list_of_words[number_of_words - 1][1])
        word_in_cloud.setSize( int(size_constant)+ 15)
        word_in_cloud.draw(wordcloud)
        #Used to draw the word in the cloud with its size set according to frequency

    buttonmaker(Point(10,2),Point(90,8),Point(50,5)\
    ,"Click anywhere to exit the progam", color_rgb(65,179,247),"black")

def stopwordRemover(words_list):

    stop_words_file = open("stop_words.txt", "r", encoding = "utf-8")
    #Used to open stop words file

    stop_words_list = stop_words_file.read().split("\n")
    #Used to get stop words in a list

    for word in words_list:
        if word in stop_words_list:
            while word in words_list:
                words_list.remove(word)
    #Used to remove all stop words from out list of words

    return words_list
    #Used to return new word list with stop words removed

def wordFrequency(file_name):

    analysis_text = open(file_name + ".txt", "r", encoding = "utf-8")
    #Used to open text file to analyze

    words = analysis_text.read().lower()
    #This loads the text into a variable and turns it into lowercase

    punctuation_remover = words.maketrans("", "", punctuation)
    list_of_words = words.translate(punctuation_remover).split()
    #Uses the translate method to remove all punctuation from the text and split it into a list

    list_of_words = stopwordRemover(list_of_words)
    #Used to remove stop words

    counts = {}
    #Used to initialise word counting dictionary

    for word in list_of_words:
        counts[word] = counts.get(word,0) + 1
    #Used to count the occurence of every word in the list

    items = list(counts.items())
    #Used to convert that dictionary into a list of tuples

    items.sort( key = byNum, reverse = True)
    #Used to sort tuples by their number of occurence

    return items
    #Used to return this list of words and their occurences


def setTitle():

    description = Text(Point(50,85), "This program can create wordclouds with input files!")
    description.setFill("black")
    description.setSize(15)
    description.setFace("arial")
    description.draw(wordcloud)
    #Used to set description

    title = Text(Point(50,95), "Wordclouds!")
    title.setFill("black")
    title.setSize(30)
    title.setFace("arial")
    title.draw(wordcloud)
    #Used to set Title

def setIntro():

    intro_button, intro_text = buttonmaker(Point(1,30),Point(99,70),Point(50,50),\
    "Welcome to the wordcloud program!\nThis program can create word clouds out of"\
    + " a\ndefault text file, or a text file of your choice!\n\nClick anywhere to continue", \
    color_rgb(65,179,247),"black", 20)
    #Introduces the program to the user

def buttonmaker(Point1,Point2,Text_point, Label, buttoncolor = "white", labelcolor = "black", labelsize = 20):

    button = Rectangle(Point1, Point2)
    button.setFill(buttoncolor)
    button.draw(wordcloud)
    #Draws button box in program
    
    buttonLabel = Text(Text_point,Label)
    buttonLabel.setFill(labelcolor)
    buttonLabel.setSize(labelsize)
    buttonLabel.draw(wordcloud)
    #Draws button label in program

    return button, buttonLabel
    #returns values of buttons to be stored as variables

def clearscreen():

    background = Rectangle(Point(0,0),Point(100,100))
    background.setFill(color_rgb(0,82,165))
    background.draw(wordcloud)
    #Used to clear the screen with a solid background

def main():

    global wordcloud
    wordcloud = GraphWin( "Wordcloud",600,600)
    wordcloud.setCoords(0,0,100,100)
    #Used to define the graphics window and make it global

    clearscreen()
    setIntro()
    #Used to set intro
    
    wordcloud.getMouse()
    #Used to wait for a mouse click

    clearscreen()
    setTitle()
    #Used to clear GUI and set the title

    buttonmaker(Point(5,45),Point(95,75),Point(50,60)\
    ,"Please enter the name of the text file you\nwish to get a wordcloud and" \
    + " the number of\nwords (between 2 and 30) you wish to get\n a wordcloud for and press continue",\
    color_rgb(65,179,247),"black")
    buttonmaker(Point(40,15),Point(60,25),Point(50,20),"Continue", color_rgb(65,179,247),"black")
    #Used to ask the user to enter their file name and draw the continue button

    global entry_text
    entry_text = Entry(Point(50,40),40)
    entry_text.setText("Frankenstein")
    entry_text.setFill(color_rgb(65,179,247))
    entry_text.draw(wordcloud)
    #Used to draw entry box for text

    global entry_number
    entry_number = Entry(Point(50,30),40)
    entry_number.setText("10")
    entry_number.setFill(color_rgb(65,179,247))
    entry_number.draw(wordcloud)
    #Used to draw entry box for numnber of words

    continue_click = clickChecker()
    #Used to get a mouseclick until user clicks continue

    file_name = entry_text.getText()
    number_of_words = int(entry_number.getText())
    #Used to get the file name and number of words

    words_list = wordFrequency(file_name)
    #Used to get the list of most common words from the file

    words_list = numwordChecker(words_list, number_of_words)
    #Makes sure no error will occur if user enters an input file with words lesser than required in wordcloud
         
    clearscreen()
    entry_text.undraw()
    entry_number.undraw()
    #Used to clear screen

    wordcloudMaker(words_list, number_of_words)
    #Used to draw the specified number of most commmon words onto the GUI in a wordcloud

    wordcloud.getMouse()
    #Used to wait for a mouselick

    wordcloud.close()
    #Used to close program

main()
