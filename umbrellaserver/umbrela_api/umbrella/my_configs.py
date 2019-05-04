from django.http import request
class DisableCSRF(object):
    def process_request(self,request):
        setattr(request,'_dont_enforce_csf_checks',True)