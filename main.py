#  SepehrRasouli 2021 , 1400 
#  Use With Caution
# ‎ Made With Love :D



from instaclient import InstaClient
from instaclient.errors.common import *
from instaclient.errors.navigator import *
import selenium.common.exceptions
import time
import datetime
import random
#Create client objectgetFlogi
client = InstaClient(driver_path="ENTER DRIVER PATH HERE")



LOGIN = None
commands = ["login","getFollowers","getFollowings","writeComment","followUser","unfollowUser","textfollowunfollow","whoUnfollowedMewho"]
class Interactive:
    def Interact(self):
        print("*"*10)
        print(""" Commands:
        login *you need to login to your instagram page to use this app* 
        usage : login <username> <password>

        getFollowers to scarpe followers 
        usage : getFollowers <targetUsername> <count>

        getFollowings to scarpe Followings 
        usage : getFollowings <targetUsername> <count>

        writeComment to write a comment on a post 
        usage: writeComment <targetPostURL> <comment>

        followUser to follow a user 
        usage : followUser <targetUsername>

        unfollowUser to unfollow a user 
        usage : unfollowUser <targetUsername>

        textfollowunfollow to unfollow or follow a user based on a text. read readme to get more info
        usage : textfollowunfollow <textfilename> 

        whoUnfollowedMe to check who unfollowed you. to use this , check readme
        usage : whoUnfollowedMe <yourusername> <yourlastfollowerslist>)""")
        print("*"*10)
        print("CAUTION : To avoid getting blocked by instagram, all actions are done with a 1 up to 3 minute delay.\n if your account gets banned , i have no responsibility.")
        print("write help to get more info")
        takeInput = input("Instagram Bot > ")
        print("*"*10)

        self.Digest(takeInput)

    def Digest(self,userInput):
        global commands
        #NOTE : On writeComment , make sure to make a system to disable sending comments after a number for a time, to avoid getting blocked by instagram
        #UPDATE : Might add psot
        userInput = userInput.split(" ")
        if userInput[0].lower() == "login":
            self.login(userInput[1],userInput[2])

        if userInput[0] in commands:
            self.Call(userInput) #To call functions
            
        else:
            print("Command Not Found.")
            self.Interact()

    def Call(self,userInput):
        global commands
        commandsStatements = {"getFollowers":"main.getFollowers(userInput)","getFollowings":"main.getFollowings(userInput)",
        "writeComment":"main.writeComment(userInput)","followUser":"main.followUser(userInput)","unfollowUser":"main.unfollowUser(userInput)",
        "textfollowunfollow":"main.textfollowunfollow(userInput)"," whoUnfollowedMe":"main.whoUnfollowedMe(userInput)"}
        if LOGIN == True:
            main = Main()
            exec(commandsStatements[userInput[0]])
        
        else:
            print("Not Logged in. Login First.")
            self.Interact()

    def login(self,username,password):
        try:
            client.login(username=username, password=password)
        except InvalidUserError:
            print("Invalid Username.")
            self.Interact()

        except InvaildPasswordError:
            print("Invalid Password.")
            self.Interact()

        except SuspisciousLoginAttemptError:
            print("IG have detectesd Suspicious Login Attempt. You need to verify your identity manualy")
            self.Interact()
        
        except selenium.common.exceptions.TimeoutException:
            print("TimedOut. Perhaps You Have Logged In Already.")
            self.Interact()

        except selenium.common.exceptions.WebDriverException:
            print("Executable needs to be in PATH")
            self.Interact()

        else:
            global LOGIN
            LOGIN = True
            print("Login succeeded. Idle for 10 secounds.")
            time.sleep(10)
            self.Interact()

class Main:
    def Beautifier(self,notBeautified) -> list:
        BeautifiedList = []
        for temp in notBeautified:
            if type(temp) == list:
                for user in temp:
                    user = str(user)
                    if user.startswith("Profile"):
                        string = ""
                        i = 0
                        while i != len(user):
                            while user[i] != "<":
                                i += 1
                                continue
                            else:
                                i += 1
                                while user[i] != ">":
                                    string += user[i]
                                    i += 1
                                else:
                                    BeautifiedList.append(''.join(string))
                                    break
                        else:
                            break
                    else:
                        continue

            else:
                pass

        return BeautifiedList

    def writeIn(self,content,name):
        nowDate = datetime.datetime.now()
        with open("%s.txt"%(name),"w") as file:
            file.write("Time : %s\n"% nowDate)
            file.write("Names:")
            for element in content:
                file.write(element+"\n")


    def Idle(self,source=None):
        if source == None:
            listOfMinutes = [60,120,180]
            minute = random.choice(listOfMinutes)
            print("Please Wait For %s Secounds."%minute)
            time.sleep(minute)
            inter = Interactive()
            inter.Interact()

        else:
            listOfMinutes = [60,120,180]
            minute = random.choice(listOfMinutes)
            print("Please Wait For %s Secounds."%minute)
            time.sleep(minute)


    def getFollowers(self,userInput):
        if type(userInput[1])  == str:
            print("This Might take some time depending on the amount of followers you want to scrape.")
            try:
                notBeautified = client.get_followers(user=userInput[1],count=int(userInput[2]))
            except InvalidUserError:
                print("Invalid Username.")
                inter = Interactive()
                inter.Interact()
            else:
                Beautified = self.Beautifier(notBeautified)
                print("Done.")
                print("List of followers : %s" % Beautified)
                self.writeIn(Beautified,"FollowersOf%s"%userInput[1])
                print("Going Idle")
                self.Idle()

        else:
            print("Invalid Username To scrape.")
            inter = Interactive()
            inter.Interact()

    def getFollowings(self,userInput):
        if type(userInput[1])  == str:
            print("This Might take some time depending on the amount of followers you want to scrape.")
            try:
                notBeautified = client.get_following(user=userInput[1],count=int(userInput[2]))
            except InvalidUserError:
                print("Invalid Username.")
                self.Idle()
            else:
                Beautified = self.Beautifier(list(notBeautified))
                print("Done.")
                print("List of Followings : %s" % Beautified)
                self.writeIn(Beautified,"Followings%s"%userInput[1])
                print("Going Idle")
                self.Idle()

        else:
            print("Invalid Username To scrape.")
            inter = Interactive()
            inter.Interact()


    def writeComment(self,userInput):
        try:
            client.comment_post(userInput[1],text=userInput[2])
        except InvalidShortCodeError:
            print("Invalid ShortCode.")
            inter = Interactive()
            inter.Interact()
        else:
            print("Done")
            print("Going Idle")
            self.Idle()

    def followUser(self,userInput):
        try:
            client.follow_user(userInput[1])
        except InvalidUserError:
            print("Invalid Username")
            inter = Interactive()
            inter.Interact()
        else:
            print("Done")
            print("Going Idle")
            self.Idle()

    def unfollowUser(self,userInput):
        try:
            client.unfollow_user(userInput[1])
        except InvalidUserError:
            print("Invalid Username")
            inter = Interactive()
            inter.Interact()
        else:
            print("Done")
            print("Going Idle")
            self.Idle()

    def whoUnfollowedMe(self,userInput):
        try:
            oldFile = open(userInput[1],"r")

        except IOError:
            print("TextFile Not Found.")
            inter = Interactive()
            inter.Interact()

        else:
            notBeautified = client.get_following(user=userInput[2],count=userInput[3])
            Followers = self.Beautifier(notBeautified)
            oldFileNotBeautified = oldFile.readlines()
            oldFileNotBeautified = list(oldFileNotBeautified)
            oldFileNotBeautified = [x.strip() for x in oldFileNotBeautified]
            if oldFileNotBeautified[0].startswith("Time : ") and oldFileNotBeautified[2].startswith("Names:"):
                oldFollowers = oldFileNotBeautified[2:]

            else:
                pass

            for oldFollower in oldFollowers:
                if oldFollower not in Followers and not oldFollower.startswith("Names:") and not oldFollower.startswith("Time : "):
                    print("%s Unfollowed you."%oldFollower)
                    continue

                else:
                    continue



    def getList(self,textfile)-> dict :
        #Returns a dictionary of who to follow and who to unfollow
        text = []
        try:
            f = open(textfile,"r")

        except IOError:
            return "File Does Not Exist"

        else:
            with open(textfile,"r") as f:
                for line in f:
                    text.append(line)

        temp = None
        text = [x.strip() for x in text]
        finalDictionary = {}
        for element in text:
            temp = element.split()
            try:
                finalDictionary[temp[0]] = temp[1]
            except IndexError:
                print("Unknown Error occurred.")
                inter = Interactive()
                inter.Interact()

        return finalDictionary

    def textfollowunfollow(self,userInput):
        finalDictionary = self.getList(userInput[1])
        if type(finalDictionary) == dict:
            for element in finalDictionary.keys():
                if finalDictionary[element].lower() == "follow":
                    print("Followed %s"%element)
                    client.follow_user(element)
                    self.Idle(True)
                    continue

                if finalDictionary[element].lower() == "unfollow":
                    print("Unfollowed %s"%element)
                    client.unfollow_user(element)
                    self.Idle(True)
                    continue

                else:
                    print("Invalid Command.")
                    continue

        else:
            print(finalDictionary)
            inter = Interactive()
            inter.Interact()

        print("Done.")
        inter = Interactive()
        
if __name__ == "__main__":
    inter = Interactive()
    inter.Interact()