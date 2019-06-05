# UmbrellaBot
"""
Este arquivo é responsavel por todas as interações entre usuarios(sessions).
aqui vai conter metodos que usam threads e criação dinamica de objetos
do tipo sessionManager();
"""
from threading import Thread
from multiprocessing.pool import ThreadPool
from time import *
from manage import ManageSessions



class UmbrellaBot(object):
    def __init__(self,username,password,param_process):
        self.username=username
        self.password=password
        self.param_process=param_process
        self.pool = ThreadPool(processes=self.param_process)
        self.sessionbot = ManageSessions(self.username,self.password)
        
    def session_follow(self):
        th_session_folow = self.pool.apply_async(self.sessionbot.session_following())
        

    def sessions_following_by_list_tags(self,tags,amount):
        th_session_following_by_list_tags = self.pool.apply_async(self.sessionbot.sessions_following_by_list_tags(tags,amount))
        
    
    def get_my_followers_of_my_sessions(self,usernameSession):
        th_session_get_my_followrs_of_my_sessions =self.sessionbot.get_my_followers_of_my_sessions(usernameSession)                                                                                                                                                                                            
        return th_session_get_my_followrs_of_my_sessions
    
    def follow_users_get_list_users(self,list_follows):
        th_session_follow_users_get_list_users = self.pool.apply_async(self.sessionbot.follow_users_get_list_users(list_follows))
        
        
    def follow_likers(self,list_users):
        th_session_follow_likers = self.pool.apply_async(self.sessionbot.follow_likers(list_users))
        
        
    def follow_coments(self,list_users):
        th_session_follow_coments = self.pool.apply_async(self.sessionbot.follow_coments(list_users))
        


a = UmbrellaBot("merynstart12","6036236",10)
result = a.get_my_followers_of_my_sessions("merynstart12")
a.sessions_following_by_list_tags(['japao','china'],15)
a.follow_likers(result)
