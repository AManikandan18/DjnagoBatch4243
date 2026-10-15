import time

class RequestLoggingMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        print("Requested URL: ",request.path) #/
        
        response = self.get_response(request) #move next middleware or View
    
        print("Response Status: ",response.status_code)
    
        return response
    
    
