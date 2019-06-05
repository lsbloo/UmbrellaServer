"""
this object sets the user session connection settings and instagram script automation
"""
from instapy import InstaPy
from instapy import smart_run
from time import sleep

class ManageSessions(object):
    def __init__(self,usernameuser,passworduser,hability_browser = False):
        self.umbrellaBot=InstaPy(username=usernameuser,password=passworduser,headless_browser=hability_browser).login()

    def session_following(self):
        print("Executing... session_following  {Status: INIT}")
        self.umbrellaBot.set_do_follow(enabled=True,percentage=10,times=2)
        print('Executing... session_following  {Status: DONE}')


    """
    follows a series of instagram profiles according to a list of specified tags the param_perfils attribute
    defines how many profiles are to be followed by that specified tag
    """
    def sessions_following_by_list_tags(self,tags,param_perfils):
        
        if len(tags) != 0:
            print('Executing.. session folloy bi list of tags {Status: INIT}')
            self.umbrellaBot.follow_by_tags(tags,amount=param_perfils)
            print('Executing... session follow by list of tags {Status: DONE}')
        else:
            print("LIST OF TAGS NULL!")


    """
    retorna todos os seguidores do user(session)
    """
    def get_my_followers_of_my_sessions(self,usernameSession,amountSession="full",live_matchSession=True,store_locallySession=False):
        print("Executing ... get followers of session {Status: Init}")
        print()
        my_list_followers=self.umbrellaBot.grab_followers(username=usernameSession,amount=amountSession,live_match=live_matchSession,store_locally=store_locallySession)
        print()
        print("Executing ... get followers of session {Status: Done}")
        return my_list_followers

    """
    dado uma lista de perfils, segue todos caso o user(session) não os siga.
    """
    def follow_users_get_list_users(self,list_follow,time=1,sleep=60,interaction=False):
        print('Executing... session follow users get list of users {Status: INIT}')
        print()
        self.umbrellaBot.follow_by_list(followlist=list_follow,times=time,sleep_delay=sleep,interact=interaction)
        print()
        print('Executing... session follow users get list of users {Status: Done}')



    """
    dado uma lista de seguidores, segue quem comentou as fotos de cada seguidor da lista;
    amount = quantidade de pessoas pesquisadas
    daysold = fotos com até 365 dias de validade
    max_pic = limita a quantidade de fotos a ser analisada
    sleep_delay = é usado para definir o tempo de pausa apos um bom numero de seguidores média 10;
    """
    def follow_coments(self,list_users,amount=100,daysold=365,max_pic=100,sleep=60, interaction=False):
        print("Executing.. follo coments of list users of session user ... {Status: Init}")
        print()
        self.umbrellaBot.follow_commenters(list_users,amount=amount,daysold=daysold,max_pic=max_pic,sleep_delay=sleep,interact=interaction)
        print()
        print("Executing.. follo coments of list users of session user ... {Status: Done}")

    """
    dado uma lista de perfils , segue outros perfis que curtiram fotos de cada membro da lista de perfil;
      -> photos_grab_amount = 2 fotos aleatorias
      -> follows_likers_per_photo = 3 quantidade de pessoas que curtiram a foto e que irão ser seguidas;
      -> randomize= True vai tirar fotos de newes, true terá aleatório dos primeiros 12
      -> sleep_delay= 60 usado para definir o tempo de pausa apos alguns bons seguidores a média é 10;
    """
    def follow_likers(self,list_users,photo_grab_amount=2, follow_likers_per_photos=3,randomize=True,sleep=60,interaction=False):
        print("Executing... follow likers of get list_users session {Status: Init} ")
        print()
        self.umbrellaBot.follow_likers(list_users,photos_grab_amount=photo_grab_amount,follow_likers_per_photo=follow_likers_per_photos,randomize=randomize,sleep_delay=sleep,interact=interaction)
        print()
        print("Executing... follow likers of get list_users session {Status: Done} ")
    """
    dado uma lista de seguidores(amigos),segue uma lista de outros seguidores amigos dos mesmos;
    """
    def follow_users_get_my_followers(self,neighour_list_followers,param_perfils,rand=False,sleep=60):
        print('Executing... neighour list followers of session user {Status: Init}')
        print()
        self.umbrellaBot.follow_user_followers(neighour_list_followers,param_perfils,rand,sleep)
        print()
        print('Executing... neighour list followers of session user {Status: Done}')
