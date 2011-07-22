class FacebookCanvasMiddleware(object):
    def process_response(self, request, response):
        if 'signed_request' in request.REQUEST:
            response.set_cookie('signed_request', request.REQUEST['signed_request'])
        response['P3P'] = 'CP="IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT"'
        
        return response
    