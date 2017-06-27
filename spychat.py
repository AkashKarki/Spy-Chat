from steganography.steganography import Steganography
from datetime import datetime
spy_list={}
spy_history={}
def Add_Status(spy_name):
    pre_status_list=["available","busy","sleeping","at work"]
    if len(spy_list[spy_name]["status"])==0:
        print"you dont have any previous status"
    else:
        print"you have previous status::"
    while True:
        status_choice=raw_input("press 1 if you want to select the status from predefined list\npress 2 to create your own status\npress 3 to select from previous status history\nwating for response")
        if status_choice=="1":
            while True:
                i=1
                for status in pre_status_list:
                    print str(i)+"."+status
                    i=i+1
                res=int(raw_input("wating for your response"))
                if res>len(pre_status_list):
                    print"\nwrong input try again"
                    continue
                new_status=pre_status_list[res-1]
                spy_list[spy_name]["present status"] =new_status
                spy_list[spy_name]["status"].append(new_status)
                print"status set"
                return
        elif status_choice=="2":
            new_status=raw_input("enter your new status")
            spy_list[spy_name]["status"].append(new_status)
            spy_list[spy_name]["present status"] = new_status
            print"status set"
            break
        elif status_choice=="3":
            print"\nyour previous status are::"
            i=1
            if len(spy_list[spy_name]["status"])==0:
                print"\nyou do not have previous status"
                continue
            else:
                for status in spy_list[spy_name]["status"]:
                    print str(i)+"."+status
                    i=i+1
                res = int(raw_input("wating for your response"))
                sta=spy_list[spy_name]["status"]
                new_status = sta[res - 1]
                spy_list[spy_name]["present status"] = new_status
                print"status set"
                break
        else:
            print"wrong choice"
            continue

def Add_friend(spy_name):
    while True:
        friend_name = raw_input("enter friend's name::")
        friend_age = int(raw_input("enter friend's age::"))
        friend_rating = raw_input("enter friend's rating::")
        if (friend_age >= 12 and friend_age <= 50) and (len(friend_name) != 0):
            if (float(spy_list[spy_name]["rating"]) <= float(friend_rating)):
                spy_list[spy_name]["friend"].update({friend_name: {"age": friend_age, "rating": friend_rating}})
                print "friend added"
                break
            else:
                print "information is not valid.Try again"
                continue
        else:
            print "information is not valid.Try again"
            continue


def Select_friend(spy_name):
    while True:
        print "please select a friend::"
        i=1
        friend_list=spy_list[spy_name]["friend"].keys()
        for friend_name in friend_list:
            print str(i)+"."+friend_name
            i=i+1
        choice=int(raw_input("wating for resonse::"))
        if choice>len(spy_list[spy_name]["friend"]):
            print "\nwrong input please input again"
            continue
        else:
            friend=friend_list[choice-1]
            return (friend)


def Send_message(spy_name,friend_pos):
    path=raw_input("enter image name::")
    out_name=raw_input("enter output image name::")
    message=raw_input("enter the message::")
    try:
        print"\nplease wait encodeing the image"
        Steganography.encode(path, out_name, message)
        print "\nmessage encription done"
        if spy_name not in spy_history.keys():
            friend_name=friend_pos
            spy_history.update({spy_name:{friend_name:{"message":[],"time":[]}}})
            spy_history[spy_name][friend_name]["message"].append(message)
            spy_history[spy_name][friend_name]["time"].append(datetime.now().strftime('%H:%M:%S'))
        else:
            friend_name = friend_pos
            if friend_name not in spy_history[spy_name].keys():
                spy_history[spy_name].update({friend_name: {"message": [], "time": []}})
            spy_history[spy_name][friend_name]["message"].append(message)
            spy_history[spy_name][friend_name]["time"].append(datetime.now().strftime('%H:%M:%S'))
    except Exception as e:
        print"image not found"
        

def read_a_message(spy_name):
    pos=Select_friend(spy_name)
    while True:
        image_name=raw_input("enter name of image you want to decode")
        try:
            print"\nplease wait decodeing the image"
            secret_text = Steganography.decode(image_name)
            print "secret message is::"+secret_text
            break
        except Exception as e:
            print "\nthis image does not contain any text"
            continue

def read_chat(spy_name):
        friend_name= Select_friend(spy_name)
        name_list=spy_history[spy_name].keys()
        if friend_name in name_list:
            message_list = spy_history[spy_name][friend_name]["message"]
            print"list of message send by "+friend_name
            for message in message_list:
                print"=>"+message
        else:
            print friend_name+" had not sent any message."

while True:
    print"Welcome Spy"
    spy_name=raw_input("enter the your name::")
    if spy_name not in spy_list.keys():
        if len(spy_name)!=0:
            spy_salutation=raw_input("\npress 1 to adress you Mr\npress 2 to adress you Ms\nwating for your response::")
            while True:
                if spy_salutation=="1":
                    spy_salutation="Mr"
                    break
                elif spy_salutation=="2":
                    spy_salutation = "Ms"
                    break
                else:
                    print "invalid option try again"
                    continue
            spy_authenticate=int(raw_input("enter your age::"))
            if spy_authenticate>=12 and spy_authenticate<=50:
                spy_rating=raw_input("enter your rating::")
                spy_list.update({spy_name:{"status":[],"present status":"","salutation":spy_salutation,"rating":spy_rating,"age":spy_authenticate,"friend":{}}})
                print"\nyou are added to spy list"
                continue
            else:
                print "\nyou are not in age limit"
                continue
        else:
            print "\ninvalid name"
            continue
    else:
        while True:
            print"welcome "+spy_list[spy_name]["salutation"]+"."+spy_name
            spy_choice=raw_input("\n1.add status\n2.add a friend\n3.send an encoded message\n4.read message\n5.read previous history\n6.exit\nwating for resonpse::")
            if spy_choice=="1":
                Add_Status(spy_name)

            elif spy_choice=="2":
                Add_friend(spy_name)

            elif spy_choice=="3":
                friend_pos=Select_friend(spy_name)
                Send_message(spy_name,friend_pos)
            elif spy_choice=="4":
                read_a_message(spy_name)

            elif spy_choice=="5":
                read_chat(spy_name)

            elif spy_choice=="6":
                print("bye! have a nice day")
                break
            else:
                print "wrong input try again"
                continue
