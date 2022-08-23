import instaloader
#from instaloader import instaloader

usuarioMaster = ""
passMaster = ""
usuarioObjetivo = "" # aca va el perfil

cookietoken = str("session-" + usuarioMaster + ".cookie")

cntig = int(0)
cntsig = int(0)
listcnt = []
listcnts = []
jsonList = []

Loader = instaloader.Instaloader()

def Login():
    global Loader
    Loader.login(usuarioMaster, passMaster)
    
def cookieLogin():
    Loader.load_session_from_file(usuarioMaster, filename=cookietoken)

def SumarCnt():
    global cntig
    global listcnt
    #while cntig <= 0:
    cntig = len(listcnt)
    cntsig = len(listcnts)
    print("Contador Actual de Seguidores: ", cntsig)
    print("Contador Actual de Siguiendo: ", cntig)

        

def Contador():
    global cntig
    profile = instaloader.Profile.from_username(Loader.context, usuarioObjetivo)

    for followee in profile.get_followees():
        listcnt.append(followee.username)
        #print(listcnt)
        #print(followee.username)
    for followers in profile.get_followers():
        listcnts.append(followers.username)
    SumarCnt()
        # se podria usar una lista y luego sumar los elementos
        
def saveJson():
    for i in range(0,len(listcnt)):
        jsonList.append({"seguidores": listcnts[i], "siguiendo": listcnt[i]})
    with open('igscrap.json', 'w') as a:
        json.dump(jsonList, f)

#Login()
cookieLogin()
Contador()
#saveJson()
