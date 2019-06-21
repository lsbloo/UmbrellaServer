"""
this object sets the user session connection settings and instagram script automation
"""
from instapy import InstaPy
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#from instabot_py import InstaBot
from instapy import smart_run
from time import sleep

class ManageSessions(object):
    def __init__(self,usernameuser,passworduser,hability_browser = True):
        self.umbrellaBot=InstaPy(username=usernameuser,password=passworduser,headless_browser=hability_browser).login()
        self.username=usernameuser
        self.password=passworduser
    

    def session_following(self):
        print("Executing... session_following  {Status: INIT}")
        self.umbrellaBot.set_do_follow(enabled=True,percentage=10,times=2)
        print('Executing... session_following  {Status: DONE}')

    def init_umbrella_toolkit(self):
        self.umbrellaBoTools = InstaBot(
        login=self.username,  # Enter username (lowercase). Do not enter email!
        password=self.password,
        like_per_day=1000,
        comments_per_day=0,
        tag_list=["follow4follow", "f4f", "cute", "l:212999109"],
        tag_blacklist=["rain", "thunderstorm"],
        user_blacklist={},
        max_like_for_one_tag=50,
        follow_per_day=300,
        follow_time=1 * 60 * 60,
        unfollow_per_day=300,
        unlike_per_day=0,
        unfollow_recent_feed=True,
        # If True, the bot will also unfollow people who dont follow you using the recent feed. Default: True
        time_till_unlike=3 * 24 * 60 * 60,  # 3 days
        unfollow_break_min=15,
        unfollow_break_max=30,
        user_max_follow=0,
        # session_file=False, # Set to False to disable persistent session, or specify custom session_file (ie ='myusername.session')
        user_min_follow=0,
        log_mod=0,
        proxy="",
        # List of list of words, each of which will be used to generate comment
        # For example: "This shot feels wow!"
        comment_list=[
            ["this", "the", "your"],
            ["photo", "picture", "pic", "shot"],
            ["is", "looks", "is 👉", "is really"],
            [
                "great",
                "super",
                "good",
                "very good",
                "good",
                "wow",
                "WOW",
                "cool",
                "GREAT",
                "magnificent",
                "magical",
                "very cool",
                "stylish",
                "beautiful",
                "so beautiful",
                "so stylish",
                "so professional",
                "lovely",
                "so lovely",
                "very lovely",
                "glorious",
                "so glorious",
                "very glorious",
                "adorable",
                "excellent",
                "amazing",
            ],
            [".", "🙌", "... 👏", "!", "! 😍", "😎"],
        ],
        # Use unwanted_username_list to block usernames containing a string
        # Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
        # 'free_followers' will be blocked because it contains 'free'
        unwanted_username_list=[
            "second",
            "stuff",
            "art",
            "project",
            "love",
            "life",
            "food",
            "blog",
            "free",
            "keren",
            "photo",
            "graphy",
            "indo",
            "travel",
            "art",
            "shop",
            "store",
            "sex",
            "toko",
            "jual",
            "online",
            "murah",
            "jam",
            "kaos",
            "case",
            "baju",
            "fashion",
            "corp",
            "tas",
            "butik",
            "grosir",
            "karpet",
            "sosis",
            "salon",
            "skin",
            "care",
            "cloth",
            "tech",
            "rental",
            "kamera",
            "beauty",
            "express",
            "kredit",
            "collection",
            "impor",
            "preloved",
            "follow",
            "follower",
            "gain",
            ".id",
            "_id",
            "bags",
        ],
        unfollow_whitelist=["example_user_1", "example_user_2"],
        # Enable the following to schedule the bot. Uses 24H
        # end_at_h = 23, # Hour you want the bot to stop
        # end_at_m = 30, # Minute you want the bot stop, in this example 23:30
        # start_at_h = 9, # Hour you want the bot to start
        # start_at_m = 10, # Minute you want the bot to start, in this example 9:10 (am).
    )

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

    # This is used to perform likes on your own feeds
    # amount=100  specifies how many total likes you want to perform
    # randomize=True randomly skips posts to be liked on your feed
    # unfollow=True unfollows the author of a post which was considered
    # inappropriate interact=True visits the author's profile page of a
    # certain post and likes a given number of his pictures, then returns to feed
     
     #-> param amount and enable interactions
    def like_by_feed_of_my_followers(self,param_perfils,interact_perfils):
        print('Executing.. like by feed of my feed followers {Status: Init}')
        print()
        self.umbrellaBot.like_by_feed(amount=param_perfils,randomize=True,
        unfollow=True,interact=interact_perfils)
        print()
        print('Executing.. like by feed of my feed followers {Status: Done}')

    

    #da likers de acordo com uma localização;
    # https://www.instagram.com/explore/locations/942720099/mosteiro-de-sao-bento-de-sao-paulo/
    # link de exploração de localizações;
    #param, localização number or path 942720099/ahsuahsuahs
    # param, amount - param-perfis;
    def like_by_localization(self,param_localization,param_perfils):
        print('Executing.. like by localization.. {Status: Init}')
        print()
        self.umbrellaBot.like_by_locations(param_localization,param_perfils)
        print()
        print('Executing.. like by localization..  {Status: Done}')

    # hidden up
    #segue de acordo com uma localização
    def follow_by_localization(self,param_localization,param_perfils):
        print('Executing.. follow by localization.. {Status: Init}')
        print()
        self.umbrellaBot.follow_by_locations(param_localization,param_perfils)
        print('Executing.. follow by localization.. {Status: Done}')
        print()
    
    #param interact: ativar interações com outros users;
    # segue uma lista de perfis determinada;
    def follows_by_list_perfis(self,list_perfis,interact):
        print('Executing.. follows_by_list_perfis.. {Status: Init}')
        print()
        self.umbrellaBot.follow_by_list(followList=list_perfis,times=1,sleep_delay=800,interact=interact)
        print('Executing.. follows_by_list_perfis.. {Status: Done}')
        print()


    # amount
    # list_perfil
    # segue quem comentou as fotos de uma determinada lista de usuarios;
    def follow_comments_by_list_perfil(self,list_perfis,param_perfis):
        print('Executing.. follow_comments_by_list_perfil.. {Status: Init}')
        print()
        self.umbrellaBot.follow_commenters(list_perfis,amount=param_perfis,daysold=365,max_pic=100,sleep_delay=800)
        print()
        print('Executing.. follow_comments_by_list_perfil.. {Status: Done}')

    #para de seguir dado uma determinada lista de perfis;   
    def unfollow_users(self,list_perfis,param_perfis):
        print('Executing.. unfollow_users.. {Status: Init}')
        print()
        self.umbrellaBot.unfollow_users(amount=84, customList=(True, list_perfis, "nonfollowers"), style="RANDOM", unfollow_after=55*60*60, sleep_delay=600)
        print('Executing.. unfollow_users.. {Status: Done}')
        print()
    
    #comenta as fotos de uma lista de perfis amigos.
    def comment_photos_friend(self,list_perfis_friends):
        self.umbrellaBot.session.set_comment_replies(replies=[u"😎😎😎", u"😁😁😁😁😁😁😁💪🏼", u"😋🎉", "😀🍬", u"😂😂😂👈🏼👏🏼👏🏼", u"🙂🙋🏼‍♂️🚀🎊🎊🎊", u"😁😁😁", u"😂",  u"🎉",  u"😎", u"🤓🤓🤓🤓🤓", u"👏🏼😉"],
                            media="Photo")

        self.umbrellaBot.set_user_interact(amount=2, percentage=70, randomize=False, media="Photo")

        self.umbrellaBot.session.set_do_like(enabled=True, percentage=94)

        self.umbrellaBot.interact_by_comments(usernames=list_perfis_friends,
                             posts_amount=10,
                             comments_per_post=5,
                             reply=True,
                             interact=True,
                             randomize=True,
                             media="Photo")