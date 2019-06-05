# UmbrellaBot
"""
Este arquivo é responsavel por todas as interações entre usuarios(sessions).
aqui vai conter metodos que usam threads e criação dinamica de objetos
do tipo sessionManager();
"""
import threading
from multiprocessing.pool import ThreadPool

from time import *
from .manage import ManageSessions



class UmbrellaBot(threading.Thread):
    def __init__(self,username,password,amount,param_process):
        threading.Thread.__init__(self)
        self.username=username
        self.password=password
        self.amount=amount
        self.param_process=param_process
        self.pool = ThreadPool(processes=self.param_process)
        self.sessionbot = ManageSessions(self.username,self.password)
        
    def run(self):
        print('init instance of threadding bot')
    def session_follow(self):
        th_session_folow = self.pool.apply_async(self.sessionbot.session_following())
        

    def sessions_following_by_list_tags(self,tags):
        th_session_following_by_list_tags = self.pool.apply_async(self.sessionbot.sessions_following_by_list_tags(tags,self.amount))
        
    
    def get_my_followers_of_my_sessions(self,usernameSession):
        th_session_get_my_followrs_of_my_sessions =self.sessionbot.get_my_followers_of_my_sessions(usernameSession)                                                                                                                                                                                            
        return th_session_get_my_followrs_of_my_sessions
    
    def follow_users_get_list_users(self,list_follows):
        th_session_follow_users_get_list_users = self.pool.apply_async(self.sessionbot.follow_users_get_list_users(list_follows))
        
        
    def follow_likers(self,list_users):
        th_session_follow_likers = self.pool.apply_async(self.sessionbot.follow_likers(list_users))
        
        
    def follow_coments(self,list_users):
        th_session_follow_coments = self.pool.apply_async(self.sessionbot.follow_coments(list_users))
