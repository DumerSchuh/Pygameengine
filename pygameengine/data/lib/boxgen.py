import os
import json
base_dir=os.path.dirname(os.path.abspath(__file__))
settings_path=os.path.join(base_dir,"..","settings.json")
with open(settings_path,"rt",encoding="utf-8") as f:
    cols=json.load(f)
class gen:
    @staticmethod
    def header(length=15,headingtext="             ",split=False,splitlength1=3,splitlength2=7,color="WHITE",setcols={}):
            try:
                if not (setcols["a"] and setcols["b"] and setcols["c"] and setcols["d"] and setcols["e"] and setcols["f"] and setcols["g"] and setcols["h"] and setcols["i"] and setcols["j"] and setcols["k"]):
                    setcols=type.type1()
            except:
                setcols=type.type1()
            length+=2
            headingtext=f" {headingtext} "
            lhead=len(headingtext)
            splitlength1+=2
            splitlength2+=2
            print(cols["colors"][color]+setcols["c"]+setcols["a"]*lhead+setcols["d"]+cols["colors"]["RESET"])
            print(cols["colors"][color]+setcols["b"]+headingtext+setcols["b"]+cols["colors"]["RESET"])
            if split==True and not (splitlength1==0 or splitlength2==0):
                splitlength=splitlength2+splitlength1+1
                if lhead>splitlength:
                    print(cols["colors"][color]+setcols["g"]+setcols["a"]*splitlength1+setcols["i"]+setcols["a"]*splitlength2+setcols["i"]+setcols["a"]*(lhead-splitlength-1)+setcols["f"]+cols["colors"]["RESET"])
                elif lhead==splitlength:
                    print(cols["colors"][color]+setcols["g"]+setcols["a"]*splitlength1+setcols["i"]+setcols["a"]*splitlength2+setcols["h"]+cols["colors"]["RESET"])
                else:
                    if lhead==splitlength1:
                        print(cols["colors"][color]+setcols["g"]+setcols["a"]*splitlength1+setcols["k"]+setcols["a"]*splitlength2+setcols["d"]+cols["colors"]["RESET"])
                    elif lhead>splitlength1:
                        print(cols["colors"][color]+setcols["g"]+setcols["a"]*splitlength1+setcols["i"]+setcols["a"]*(lhead-splitlength1-1)+setcols["j"]+setcols["a"]*(splitlength2-(lhead-splitlength1-1)-1)+setcols["d"]+cols["colors"]["RESET"])
                    else:
                        print(cols["colors"][color]+setcols["g"]+setcols["a"]*lhead+setcols["j"]+setcols["a"]*(splitlength1-lhead-1)+setcols["i"]+setcols["a"]*splitlength2+setcols["d"]+cols["colors"]["RESET"])
            else:
                if lhead>length:
                    print(cols["colors"][color]+setcols["g"]+setcols["a"]*length+setcols["i"]+setcols["a"]*(lhead-length-1)+setcols["f"]+cols["colors"]["RESET"])
                elif lhead==length:
                    print(cols["colors"][color]+setcols["g"]+setcols["a"]*length+setcols["h"]+cols["colors"]["RESET"])
                else:
                    print(cols["colors"][color]+setcols["g"]+setcols["a"]*lhead+setcols["j"]+setcols["a"]*(length-lhead-1)+setcols["d"]+cols["colors"]["RESET"])
    @staticmethod
    def text(text="          ",split=False,text1="   ",text2="       ",color="WHITE",setcols={}):
        if not (len(setcols["a"]) and len(setcols["b"]) and len(setcols["c"]) and len(setcols["d"]) and len(setcols["e"]) and len(setcols["f"]) and len(setcols["g"]) and len(setcols["h"]) and len(setcols["i"]) and len(setcols["j"]) and len(setcols["k"])):
            setcols=type.type1()
        if split==True:
            print(cols["colors"][color]+setcols["b"]+" "+text1+" "+setcols["b"]+" "+text2+" "+setcols["b"]+cols["colors"]["RESET"])
        else:
            print(cols["colors"][color]+setcols["b"]+" "+text+" "+setcols["b"]+cols["colors"]["RESET"])
    @staticmethod
    def rowsplitter(length=10,split=False,splitlength1=3,splitlength2=7,color="WHITE",setcols={}):
        if not (len(setcols["a"]) and len(setcols["b"]) and len(setcols["c"]) and len(setcols["d"]) and len(setcols["e"]) and len(setcols["f"]) and len(setcols["g"]) and len(setcols["h"]) and len(setcols["i"]) and len(setcols["j"]) and len(setcols["k"])):
            setcols=type.type1()
        length+=2
        if split==True:
            splitlength1+=2
            splitlength2+=2
            print(cols["colors"][color]+setcols["g"]+setcols["a"]*splitlength1+setcols["k"]+setcols["a"]*splitlength2+setcols["h"]+cols["colors"]["RESET"])
        else:
            print(cols["colors"][color]+setcols["g"]+setcols["a"]*length+setcols["h"]+cols["colors"]["RESET"])
    @staticmethod
    def footer(length=10,inputbelow=False,split=False,splitlength1=3,splitlength2=7,color="WHITE",setcols={}):
        if not (len(setcols["a"]) and len(setcols["b"]) and len(setcols["c"]) and len(setcols["d"]) and len(setcols["e"]) and len(setcols["f"]) and len(setcols["g"]) and len(setcols["h"]) and len(setcols["i"]) and len(setcols["j"]) and len(setcols["k"])):
            setcols=type.type1()
        length+=2
        fd=setcols["e"]
        if inputbelow==True:
            fd=setcols["g"]
        if split==True:
            splitlength1+=2
            splitlength2+=2
            print(cols["colors"][color]+fd+setcols["a"]*splitlength1+setcols["j"]+setcols["a"]*splitlength2+setcols["f"]+cols["colors"]["RESET"])
        else:
            print(cols["colors"][color]+fd+setcols["a"]*length+setcols["f"]+cols["colors"]["RESET"])
    @staticmethod
    def input(prompt=" ",color="WHITE",setcols={}):
        if not (len(setcols["a"]) and len(setcols["b"]) and len(setcols["c"]) and len(setcols["d"]) and len(setcols["e"]) and len(setcols["f"]) and len(setcols["g"]) and len(setcols["h"]) and len(setcols["i"]) and len(setcols["j"]) and len(setcols["k"])):
            setcols=type.type1()
        full_prompt=setcols["e"]+cols["pr"]+" "+prompt
        return input(cols["colors"][color]+full_prompt+cols["colors"]["RESET"])
class type:
    def type1():
        return {"a":cols["r1a"],"b":cols["r1b"],"c":cols["r1c"],"d":cols["r1d"],"e":cols["r1e"],"f":cols["r1f"],"g":cols["r1g"],"h":cols["r1h"],"i":cols["r1i"],"j":cols["r1j"],"k":cols["r1k"]}
    def type2():
        return {"a":cols["r2a"],"b":cols["r2b"],"c":cols["r2c"],"d":cols["r2d"],"e":cols["r2e"],"f":cols["r2f"],"g":cols["r2g"],"h":cols["r2h"],"i":cols["r2i"],"j":cols["r2j"],"k":cols["r2k"]}
    def type3():
        return {"a":cols["r2a"],"b":cols["r1b"],"c":cols["r3a"],"d":cols["r3b"],"e":cols["r3c"],"f":cols["r3d"],"g":cols["r3e"],"h":cols["r3f"],"i":cols["r3g"],"j":cols["r3h"],"k":cols["r3i"]}
    def type4():
        return {"a":cols["r1a"],"b":cols["r2b"],"c":cols["r4a"],"d":cols["r4b"],"e":cols["r4c"],"f":cols["r4d"],"g":cols["r4e"],"h":cols["r4f"],"i":cols["r4g"],"j":cols["r4h"],"k":cols["r4i"]}
    def type5():
        return {"a":cols["r1a"],"b":cols["r1b"],"c":cols["r5a"],"d":cols["r5b"],"e":cols["r5c"],"f":cols["r5d"],"g":cols["r1g"],"h":cols["r1h"],"i":cols["r1i"],"j":cols["r1j"],"k":cols["r1k"]}
    def type6():
        return {"a":cols["r6a"],"b":cols["r6c"],"c":cols["r1c"],"d":cols["r1d"],"e":cols["r1e"],"f":cols["r1f"],"g":cols["r1g"],"h":cols["r1h"],"i":cols["r1i"],"j":cols["r1j"],"k":cols["r1k"]}
    def type7():
        return {"a":cols["r6b"],"b":cols["r6d"],"c":cols["r1c"],"d":cols["r1d"],"e":cols["r1e"],"f":cols["r1f"],"g":cols["r1g"],"h":cols["r1h"],"i":cols["r1i"],"j":cols["r1j"],"k":cols["r1k"]}
    def type8():
        return {"a":cols["r7a"],"b":cols["r7b"],"c":cols["r1c"],"d":cols["r1d"],"e":cols["r1e"],"f":cols["r1f"],"g":cols["r1g"],"h":cols["r1h"],"i":cols["r1i"],"j":cols["r1j"],"k":cols["r1k"]}
    def type9():
        return {"a":cols["r8a"],"b":cols["r8b"],"c":cols["r1c"],"d":cols["r1d"],"e":cols["r1e"],"f":cols["r1f"],"g":cols["r1g"],"h":cols["r1h"],"i":cols["r1i"],"j":cols["r1j"],"k":cols["r1k"]}
    def type10():
        return {"a":cols["r9a"],"b":cols["r9b"],"c":cols["r1c"],"d":cols["r1d"],"e":cols["r1e"],"f":cols["r1f"],"g":cols["r1g"],"h":cols["r1h"],"i":cols["r1i"],"j":cols["r1j"],"k":cols["r1k"]}
def pregen(text:list[str]=["          ","   "],splitteratpos:list[int]=[],headingtext:str="     ",input:bool=False,inputtext:str="",split:bool=False,splittext1:list[str]=["   "],splittext2:list[str]=["       "],color="WHITE",typ=1):
    if typ==2:
        typ=type.type2()
    elif typ==3:
        typ=type.type3()
    elif typ==4:
        typ=type.type4()
    elif typ==5:
        typ=type.type5()
    elif typ==6:
        typ=type.type6()
    elif typ==7:
        typ=type.type7()
    elif typ==8:
        typ=type.type8()
    elif typ==9:
        typ=type.type9()
    elif typ==10:
        typ=type.type10()
    else:
        typ=type.type1()
    maxlen1=max(len(t1) for t1 in splittext1) if splittext1 else 0
    maxlen2=max(len(t2) for t2 in splittext2) if splittext2 else 0
    length=max(len(t) for t in text)
    if split==True:
        length=maxlen1+maxlen2
    gen.header(length=length,headingtext=headingtext,split=split,splitlength1=maxlen1,splitlength2=maxlen2,color=color,setcols=typ)
    lines=[]
    liness1=[]
    liness2=[]
    if split==True:
        for i in range(len(text)):
            liness1.append(splittext1[i]+" "*(maxlen1-len(splittext1[i])))
            liness2.append(splittext2[i]+" "*(maxlen2-len(splittext2[i])))
    else:
        for i in range(len(text)):
            lines.append(text[i]+" "*(length-len(text[i])))    
    
    for i in range(len(text)):
        if i in splitteratpos:
            gen.rowsplitter(length=length,split=split,splitlength1=maxlen1,splitlength2=maxlen2,color=color,setcols=typ)
        if split==True:
            gen.text(split=split,text1=liness1[i],text2=liness2[i],color=color,setcols=typ)
        else:
            gen.text(text=lines[i],split=split,color=color,setcols=typ)
    gen.footer(length=length,inputbelow=input,split=split,splitlength1=maxlen1,splitlength2=maxlen2,color=color,setcols=typ)
    if input==True:
        return gen.input(prompt=inputtext,color=color,setcols=typ)
    
pregen(typ=10,text=["                       ","","","","","",""])
