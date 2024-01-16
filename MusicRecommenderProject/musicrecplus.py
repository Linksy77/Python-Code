# Belal Eltemsah, Cecilia Esteban, Jacob Franco-Wadley
# CS115 
# I pledge my honor that I have abided by the Stevens Honor System.

import os.path
PREF_FILE = 'musicrec-store.txt'
userDict = {}

def loadUsers(fileName):
    '''Reads in a file of stored users' preferences stored in the file
    'fileName'. Returns a dictionary containing a mapping of user names
    to a list of preferred artists.
        Author: Belal'''
    if os.path.exists(fileName):
        with open(fileName, 'r') as file:
            for line in file:
                [userName,artists] = line.strip().split(":")
                artistList = artists.split(",")
                artistList.sort()
                userDict[userName] = artistList
        return userDict
    else:
        with open(fileName, 'w') as file:
            pass
        return userDict

def saveUserPreferences(userName, prefs, userMap, fileName):
    '''Writes all of the user preferences to the file. Returns nothing.
        Author: Belal'''
    userMap[userName] = prefs
    file = open(fileName, "w")
    for user in userMap:
        toSave = str(user) + ":" + ",".join(userMap[user]).title() + \
                "\n"
        file.write(toSave)
    file.close()

def getUser():
    '''receives user's name and whether or not $
    Author: Jacob'''
    print('Enter your name (put a $ symbol after your name if you wish your preferences to remain private): ')
    userName=input()
    return userName

def menu():
    '''prints menu options
    Author: Jacob'''
    print("Enter a letter to choose an option:")
    print ("e - Enter preferences")
    print ("s - Show preferences")
    print ("r - Get recommendations")
    print ("d - Delete preferences")
    print ("p - Show most popular artists")
    print ("h - How popular is the most popular")
    print ("m - Which user has the most likes")
    print ("q - Save and quit")

def getPref(userName, userMap):
    '''Returns a list of the user's new preferred artists along with any old ones that weren't newly mentioned.
    Author: Jacob'''
    newPref = ''
    if userName in userMap:
        prefs = userMap[userName]
        print('I see that you have used this system before.')
        print('Your music preferences include: ')
        for artists in prefs:
            print(artists)
        print('Please enter another artist or band that you like ( Enter to finish ): ')
        newPref = input()
    else:
        prefs = []
        print('I see that you are a new user.')
        print('Enter an artist that you like ( Enter to finish ): ')
        newPref = input()
    while newPref != '':
        prefs.append(newPref.strip().title())
        print('Please enter another artist or band that you like ( Enter to finish ): ')
        newPref = input()
        prefs.sort()
    saveUserPreferences(userName, prefs, userMap, 'musicrecplus.txt')
    return prefs
    
def findBestUser(currUser, prefs, userMap):
    '''finds the user whos prefs are most similar to the current user. (Returns the best users name as a string)
    Author : Jacob'''
    bestUser = None
    bestScore= -1
    bestNumOfRecs = -1
    for user in userMap.keys():
        if currUser != user:
            score = numMatches(prefs, userMap[user])
            numOfRecs = len(userMap[user]) - score
            if score == bestScore:
                if numOfRecs > bestNumOfRecs:
                    bestNumOfRecs = numOfRecs
                    bestScore = score
                    bestUser = user
            elif score > bestScore and numOfRecs > 0:
                bestNumOfRecs = numOfRecs
                bestScore = score
                bestUser = user
    return bestUser

def drop(list1, list2):
    ''' returns a new list that contains only elements in list 2 that weren't in list1.
    Author: Jacob'''
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i+=1
            j+=1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j+=1
    while j < len(list2):
        list3.append(list2[j])
        j+=1
    return list3

def numMatches(list1, list2):
    '''returns the elements that match between two lists
    Author: Jacob'''
    matches = 0
    for artistL1 in list1:
        for artistL2 in list2:
            if artistL1 == artistL2:
                matches += 1
                break
    return matches
    
def getRecommendations(currUser, prefs, userMap):
    '''Gets recomendations for a current user based on the most similar pref list in one
    of the users in UserMap. Returns the list of recommended artists.
    Author: Jacob'''
    if len(userMap) <= 1:
        print('Error: only one user in system. Sorry!')
        return None
    bestUser = findBestUser(currUser, prefs, userMap)
    print(userMap[bestUser])
    print(prefs)
    print(drop(prefs, userMap[bestUser]))
    recommendations = drop(prefs,userMap[bestUser])
    return recommendations

def artistDictInit(userMap):
    ''' Creates a dictionary with artist names as keys and the
        number of users that like them as their value.
        Author: Cecilia
    '''
    artistDict = {}
    for user in userMap.keys():
        if user[-1] != "$":
            for artist in userMap[user]:
                if artist in artistDict:
                    artistDict[artist] += 1
                else:
                    artistDict[artist] = 1
    return artistDict

def mostPopularName(userMap):
    ''' Prints the top 3 artists that are liked by the most users.
        Author: Cecilia
    '''
    artistDict = artistDictInit(userMap)
    if len(artistDict.items()) == 0:
        return False
    sortedPopularities = sorted(artistDict.items(), key = lambda x : x[1], reverse = True)[:3]
    return list(map(lambda x : x[0], sortedPopularities))
        
def mostPopularVotes(userMap):
    ''' Returns the number of likes the most popular artist received.
        Author: Cecilia
    '''
    artistDict = artistDictInit(userMap)
    topArtist = sorted(artistDict.items(), key = lambda x : x[1], reverse = True)[0]
    return topArtist[1]

def deletePref(userName, userMap):
    ''' Removes preferences from musicrecplus.txt.
        Author: Cecilia
    '''
    prefs = userMap[userName]
    print("You current preferences include: ")
    for artist in prefs:
        print(artist)
    prefToDel = ""
    while True:
        print("Please enter the artist or band that you wish\nto be deleted from your preferences, or just press Enter:\n")
        prefToDel = input()
        if len(prefToDel) == 0:
            break
        userMap[userName] = sorted(filter(lambda x: x != prefToDel, userMap[userName]))
    return userMap[userName]

def showPref(userName, userMap):
    ''' Prints the current user's preferences.
        Author: Cecilia
    '''
    prefs = userMap[userName]
    print("You current preferences include: ")
    for artist in prefs:
        print(artist)

def mostArtists(userMap):
    '''Returns user with the most artists, one per line
        Author: Belal'''
    maxLen = 0
    user = []
    for userName, lst in userMap.items():
        if userName[-1] != '$' and len(lst) == maxLen:
            user.append(userName)
        elif userName[-1] != '$' and len(lst) > maxLen:
            maxLen = len(lst)
            user = [userName]
    return user

def main():
    '''Runs the main functionality of the program.
        Author: Belal'''
    if not os.path.isfile('musicrecplus.txt'):
        with open('musicrecplus.txt', 'w') as file:
            pass
    with open('musicrecplus.txt', 'a') as file:
        fileName = 'musicrecplus.txt'
        userDict = loadUsers(fileName)
        print("Welcome to the Music Recommender Plus.")
        userName = getUser()
        prefs = getPref(userName, userDict)
        while True:
            menu()
            userInput = input()
            if userInput == 'e':
                getPref(userName, userDict)
            elif userInput == 's':
                showPref(userName, userDict)
            elif userInput == 'd':
                prefs = deletePref(userName, userDict)
            elif userInput == 'r':
                recs = getRecommendations(userName, prefs, userDict)
                if recs == None:
                    print("No recommendations available at this time.")
                else:
                    for recommendation in recs:
                        print(recommendation)
            elif userInput == 'p':
                popular = mostPopularName(userDict)
                if not popular:
                    print("Sorry, no artists found.")
                else:
                    for artist in popular:
                        print(artist)
            elif userInput == 'h':
                popular = mostPopularVotes(userDict)
                if not popular:
                    print("Sorry, no artists found.")
                else:
                    print(popular)
            elif userInput == 'm':
                popular = mostArtists(userDict)
                if not popular:
                    print("Sorry, no user found.")
                else:
                    for user in popular:
                        print(user)
            elif userInput == 'q':
                saveUserPreferences(userName, prefs, userDict, fileName)
                break
            else:
                print("Invalid input.")
            
main()
