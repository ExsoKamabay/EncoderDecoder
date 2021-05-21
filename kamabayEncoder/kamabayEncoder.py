import json
"""@copyright exso kamabay
    This code can be modified by anyone but not for sale or purchase, 
    include the address of this repository every time it is shared

    Kode ini dapat dimodifikasi oleh siapa saja tetapi tidak untuk dijual atau dibeli,
    sertakan alamat repositori ini setiap kali dibagikan    """

def codes(auth=None) -> str:
    dic = {}
    if auth == None:return None
    elif auth == "kamabay":
        dic["xc"] = {" ":"4%32",
            "a":"!@$#%","b":"*&^)*","c":"!@#$%","d":"~gd!2",
            "e":"fgdgf","f":"es^$f","g":"ifaqd","h":"$dsew",
            "i":"feswe","j":"rh-+e","k":"xnxx&","l":"me&yu",
            "m":"vuvue","n":"gereg","o":"p039=","p":"dfe12",
            "q":"htewq","r":"3sdfh","s":"edwqe","t":"p56da",
            "u":"po;pd","v":"erf^e","w":"^'-hd","~":"&wyad",
            "x":"efwss","y":"u`u!y","z":"jsdf3","`":"!3+5h",
            "!":"$4asq","#":"*90ay","$":"&fasf","%":"ajdxa",
            "^":"-9sh!","&":"*hsf@","*":"od_+$","(":"-ajf*",
            ")":"i8atg","_":"eaqxd","-":"idnc;","+":"shcn-",
            "=":"*_*!+","{":"-9ajd","[":"hsbx7","}":"0)9ad",
            "]":"afxja","|":"jabzx","/":"fwstg",":":"havxa",
            ";":"'=.,l","'":"ksbks",'"':'nhsxc',"<":",.ihs",
            ",":"ks/,;",">":"fj-35",".":"ad/?s","?":"ksb1@",
            "1":str(float(1  * 1000 % 2  + 3  - 4  / 14 )),
            "2":str(float(2  * 1000 % 3  + 4  - 5  / 6 )),
            "3":str(float(3  * 1000 % 4  + 5  - 6  / 7 )),
            "4":str(float(4  * 1000 % 5  + 6  - 6  / 14 )),
            "5":str(float(5  * 1000 % 6  + 7  - 7  / 9 )),
            "6":str(float(6  * 1000 % 7  + 8  - 8  / 14 )),
            "7":str(float(7  * 1000 % 8  + 9  - 9  / 11 )),
            "8":str(float(8  * 1000 % 9  + 10 - 10 / 12 )),
            "9":str(float(9  * 1000 % 10 + 11 - 11 / 13 )),
            "0":str(float(10 * 1000 % 11 + 12 - 12 / 14 ))}
        return dic['xc']
    else:return "Invalid"

class KAMABAY_ENCODE_DECODE:
    def __init__(self,data:str,save:bool) -> None:
        self.data = data;
        self.save = save;
    # save data file
    def savefile(self,dataINPUT):
        with open("data.kmy","w") as f:
            f.write(dataINPUT)
            f.close()
    # load data
    @property
    def loaddata(self):
        if self.data[-4:] == ".kmy":
            with open(self.data,'r') as f:
                return f.read()
        else:return self.data

    # encrypt data
    def encode(self):
        self.list_rst = []
        self.results  = ''
        for i in self.loaddata:
            if i in codes('kamabay').keys():
                self.list_rst.append(codes('kamabay')[i])
            else:return TypeError(self.loaddata)
        for i in self.list_rst:
            self.results += i +'[KMY]'
        if self.save == True:
            self.savefile(self.results);
            return self.results;
        else:return self.results;
    # decrypt data
    def decode(self):
        def set_string(data:str):
            repla = data.replace("[KMY]"," ")
            return repla.split()
        self.str = set_string(self.loaddata)
        self.rst = ''
        for i in self.str:
            if i in codes('kamabay').values():
                for x,y in codes('kamabay').items():
                    if i in y:
                        self.rst += x;
                    else:pass;
            else:
                return f"KeyError {KeyError(self.loaddata)}"
        if self.save == True:
            self.savefile(self.rst);
            return self.rst;
        else:return self.rst;
    # show dictionary encrypt,decrypt
    def showDict(self,auth):
        if not auth:return None
        elif auth == "KAMABAY":
            return json.dumps(codes('kamabay'),indent=2,sort_keys=True)
        else:return "Invalid"
    
    def __str__(self) -> str:
        return """
        
        Nama class  : KAMABAY_ENCODE_DECODE
        __init__(self,data:str,save:bool) -> None:
        Argument :
        1. data : data input type string
        2. save : menyimpan data dalam file saat mengeluarkan, type boolean

        Nama method : 
        1. decode()
        2. encode()
        3. showDict(auth="KAMABAY"),
        4. loaddata @property
        5. savefile()
        """
