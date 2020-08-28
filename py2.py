def saybye():
    print("bye!!!!!!")
def sayhello():
    print ("helloooooooooo!!!")
def ftmd1():
    print("TMD one")
def ftmd2():
    print("TMD two")
def ftmd3():
    print("TMD three")
tmd1={
        "name":"tmd1",
        "type":"command",
        "exec":ftmd1
        }
tmd2={
        "name":"tmd2",
        "type":"command",
        "exec":ftmd2
        }
tmd3={
        "name":"tmd3",
        "type":"command",
        "exec":ftmd3
        }
quiting={
        "name":"quit",
        "type":"wo hen meng"
        }
#: the dict name cant be same with the exec name :)
cmd3list=(tmd1,tmd2,tmd3,quiting)
cmd1={
        "name":"sahello",
        "type":"command",
        "exec":sayhello
        }
cmd2={
        "name":"saybye",
        "type":"command",
        "exec":saybye
        }
cmd3={
        "name":"chat",
        "type":"list",
        "list":cmd3list
        }
cmdlist=(cmd1,cmd2,cmd3)

lastcmd=[]
hadfirstmenu=0
def menu(cl):
    global hadfirstmenu
    global lastcmd
    if hadfirstmenu==0:
        lastcmd=[cl]
        hadfirstmenu=1
    for item in cl:
        print(cl.index(item)+1,item["name"],end=" ")
    print("\n===M-E-N-U===")
    while 1:
        indexstr=input("\rselect the index of command:")
        if indexstr.isdigit():
            index=int(indexstr)
            if index>0 and index<=len(cl):
                index-=1
                break
    if cl[index]["type"]=="command":
        cl[index]["exec"]()
        menu(lastcmd[len(lastcmd)-1])
    elif cl[index]["name"]=="quit":
        lastcmd.pop(len(lastcmd)-1)
        menu(lastcmd[len(lastcmd)-1])
    elif cl[index]["type"]=="list":
        lastcmd.append(cl[index]["list"])
        menu(cl[index]["list"])
#menu(cmdlist)
# second : use config to run a program.. so this dict will save in a file,utill you call them
