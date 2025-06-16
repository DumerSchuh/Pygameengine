import os
import json
from data.lib import tools
from data.lib import boxgen
base_dir=os.path.dirname(os.path.abspath(__file__))
langsel=tools.loadsellang()
accountknow=None
pin=None
selectedsave=None
lang=tools.loadlang(langsel)
cols=tools.loadsettings()
class main:
    def run():
        global langsel,accountknow
        acc_path=os.path.join(base_dir,"data\\accounts","accknow.json")
        with open(acc_path,"rt",encoding="utf-8") as f:
            accountknow=json.load(f)
        if accountknow["loggedinbefore"]== "False":
            lines=[lang["language"]["welcomeselect"]]
            for code,name in lang["language"]["languages"].items():
                lines.append(f"{code}: {name}")
            langsel=boxgen.pregen(text=lines,splitteratpos=[1],headingtext=lang["language"]["header"],input=True,inputtext=lang["language"]["asklang"],typ=2)
            if langsel==code or name in lang["language"]["languages"]:
                pass
            else:
                langsel="en"
            accounts_path=os.path.join(base_dir,"data\\accounts","sellang.json")
            try:
                if os.path.exists(accounts_path):
                    with open(accounts_path,"rt",encoding="utf-8") as f:
                        accountknow=json.load(f)
                else:
                    accountknow={}
            except json.JSONDecodeError:
                accountknow={}
            accountknow["selectlang"]=langsel
            with open(accounts_path,"wt",encoding="utf-8") as f:
                json.dump(accountknow,f,ensure_ascii=False,indent=2)
            tools.loadlang(langsel)
            tools.clear()
            main.accmenu()
        else:
            main.accmenu()
    def accmenu():
        global accountknow,pin
        acc_path=os.path.join(base_dir,"data\\accounts","accknow.json")
        with open(acc_path,"rt",encoding="utf-8") as f:
            accountknow=json.load(f)
        if accountknow["loggedinbefore"]=="True":
            enteredPin=boxgen.pregen(text=[lang["pin"]["enterpin"]],input=True,typ=1,headingtext=lang["pin"]["header"])
            if enteredPin==tools.hashde(accountknow["pin"],tools._key_stream("pin",254)):
                tools.clear()
                boxgen.pregen(text=[lang["pin"]["callloggedin"]],headingtext=lang["pin"]["header"],typ=3)
                tools.enterclear()
                main.saves()
            else:
                tools.clear()
                boxgen.pregen(color="RED",text=["Error: 01-001--01-003"],headingtext=lang["error"]["header"],typ=4)
                tools.enterclear()
        else:
            tools.clear()
            pin=boxgen.pregen(text=[lang["pin"]["createpin"]],input=True,headingtext=lang["pin"]["header"])
            accountknow["pin"]=tools.hashen(pin,tools._key_stream("pin",254))
            accountknow["loggedinbefore"]="True"
            with open(acc_path,"wt",encoding="utf-8") as f:
                json.dump(accountknow,f,ensure_ascii=False,indent=2)
            tools.clear()
            main.accmenu()
    def saves():
        global selectedsave
        acc_path=os.path.join(base_dir,"data\\accounts","accknow.json")
        with open(acc_path,"rt",encoding="utf-8") as f:
            accountknow=json.load(f)
        lines=[]
        lines.append(lang["savemenu"]["yoursaves"])
        if accountknow.get("saves"):
            for index,(code,name) in enumerate(accountknow["saves"].items(),start=1):
                lines.append(f"{cols["qkv"]} {index}. {accountknow["saves"][str(index)]["name"]}")
            lines.append(f"{cols["qkv"]} {len(lines)}. {lang["savemenu"]["askselectsavecreate"]}")
            max_len=max(len(line) for line in lines)
            tools.clear()
            try:
                selectedsave=int(boxgen.pregen(text=lines,headingtext=lang["savemenu"]["header"],input=True,typ=2))
                tools.clear()
                if selectedsave==(len(lines)-1):
                    main.createsave()
                elif 1<=selectedsave<=(len(accountknow["saves"])):
                    main.editsave()
            except ValueError:
                selectedsave=None
                boxgen.pregen(color="RED",text=["Error: 01-001"],headingtext=lang["error"]["header"],typ=4)
                tools.enterclear()
        else:
            tools.clear()
            boxgen.pregen(text=[lang["savemenu"]["yoursaves"],lang["savemenu"]["nosaves"],lang["savemenu"]["nosavesinfo"]],headingtext=lang["savemenu"]["header"],typ=4)
            tools.enterclear()
            main.createsave()
    def createsave():
        acc_path=os.path.join(base_dir,"data\\accounts","accknow.json")
        with open(acc_path,"rt",encoding="utf-8") as f:
            accountknow=json.load(f)
        newsavename=boxgen.pregen(text=[lang["createsave"]["newsavenameenterinfo"]],typ=1,headingtext=lang["createsave"]["header"],input=True)
        if newsavename=="":
            newsavename="New Save"
        existids=[int(k) for k in accountknow["saves"].keys()]
        used_ids=sorted([int(k) for k in accountknow["saves"].keys()])
        next_id=1
        for i in used_ids:
            if i != next_id:
                break
            next_id+=1
        newsaveid=str(next_id)
        newsave={"name":newsavename,"directory":f"s{newsaveid}.json"}
        accountknow["saves"][newsaveid]=newsave
        with open(acc_path,"wt",encoding="utf-8") as f:
            json.dump(accountknow,f,ensure_ascii=False,indent=2)
        pathx=os.path.join(base_dir,"data\\accounts\\saves",f"s{newsaveid}.json")
        with open(pathx,"x",encoding="utf-8") as f:
            json.dump(cols["standartdata"],f,ensure_ascii=False,indent=2)
        tools.clear()
        boxgen.pregen(text=[lang["createsave"]["newsavecreated"]],headingtext=lang["createsave"]["header"])
        tools.enterclear()
        main.saves()

    def editsave():
        global selectedsave
        acc_path=os.path.join(base_dir,"data\\accounts","accknow.json")
        with open(acc_path,"rt",encoding="utf-8") as f:
            accountknow=json.load(f)
        saveinfo=accountknow["saves"][str(selectedsave)]
        actions=[lang["editsave"]["load"],lang["editsave"]["delete"],lang["editsave"]["rename"],lang["editsave"]["pathcopy"]]
        lines=[lang["editsave"]["askselectedsave"]+saveinfo["name"]]
        for i,action in enumerate(actions,start=1):
            lines.append(f"{cols['qkv']} {i}. {action}")
        longest=max(len(line) for line in lines)
        
        try:
            selectedaction=int(boxgen.pregen(text=lines,headingtext=lang["editsave"]["header"],typ=3,input=True,inputtext=lang["editsave"]["askselectedsave"]))
            tools.clear()
            if selectedaction==1:
                game.main()
            elif selectedaction==2:
                main.editsaveactions.delete(saveinfo)
            elif selectedaction==3:
                main.editsaveactions.rename(accountknow,acc_path)
            elif selectedaction==4:
                main.editsaveactions.copypath(accountknow,selectedsave)
            else:
                raise ValueError
        except ValueError:
            tools.clear()
            boxgen.pregen(color="RED",text=["Error: 01-001--01-003"],headingtext=lang["error"]["header"],typ=4)
            tools.enterclear()
    class editsaveactions():
        def delete(saveinfo):
            global selectedsave
            selected_key=str(selectedsave)
            conf=boxgen.pregen(text=[lang["editsave"]["confirmdelete"]+saveinfo["name"],lang["editsave"]["confirmdeleteinfo"]+saveinfo["name"]],typ=3,input=True,inputtext=lang["standart"]["booleananswer"]).strip().lower()
            yansw=[k.lower() for k,v in lang["standart"]["booleanansweroptions"].items() if v.lower()=="yes"]
            if conf in yansw:
                acc_path=os.path.join(base_dir,"data\\accounts","accknow.json")
                with open(acc_path,"rt",encoding="utf-8") as f:
                    accountknow=json.load(f)
                saves=accountknow["saves"]
                last_index=str(len(saves))
                selected_file=os.path.join(base_dir,"data\\accounts\\saves",f"s{selected_key}.json")
                if selected_key!=last_index:
                    if os.path.exists(selected_file):
                        os.remove(selected_file)
                    old_path=os.path.join(base_dir,"data\\accounts\\saves",saves[last_index]["directory"])
                    new_filename=f"s{selected_key}.json"
                    new_path=os.path.join(base_dir,"data\\accounts\\saves",new_filename)
                    if os.path.exists(old_path):
                        os.rename(old_path,new_path)
                    saves[selected_key]=saves[last_index]
                    saves[selected_key]["directory"]=new_filename
                del saves[last_index]
                with open(acc_path,"wt",encoding="utf-8") as f:
                    json.dump(accountknow,f,ensure_ascii=False,indent=2)
            else:
                tools.clear()
                boxgen.pregen(text=[lang["editsave"]["confirmdeletecanceled"]],headingtext=lang["editsave"]["header"],typ=3)
                tools.enterclear()
        def rename(accountknow,acc_path):
            newname=boxgen.pregen(text=[lang["editsave"]["renameask"]],input=True,headingtext=lang["editsave"]["header"])
            oldname=accountknow["saves"][str(selectedsave)]["name"]
            accountknow["saves"][str(selectedsave)]["name"]=newname
            with open(acc_path,"wt",encoding="utf-8") as f:
                json.dump(accountknow,f,ensure_ascii=False,indent=2)
            tools.clear()
            boxgen.pregen(text=[lang["editsave"]["renamedone1"]+oldname+lang["editsave"]["renamedone2"]+newname],typ=3,headingtext=lang["editsave"]["header"])
            tools.enterclear()
            main.saves()
        def copypath(accountknow,selectedsave):
            file=accountknow["saves"][str(selectedsave)]["directory"]
            path=os.path.abspath(os.path.join(base_dir,"data\\accounts\\saves",file))
            boxgen.pregen(text=[lang["editsave"]["copypath"]+accountknow["saves"][str(selectedsave)]["name"]+cols["dc"],path],headingtext=lang["editsave"]["header"])
            tools.enterclear()
            main.saves()
class game:
    def main():
        return
if __name__=="__main__":
    tools.clear()
    main.run()
