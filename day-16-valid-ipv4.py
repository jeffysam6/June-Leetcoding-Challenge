class Solution:
    def validIPAddress(self, IP: str) -> str:
        
        if('.' in IP):
            
            s = IP.split('.')
            
            
            for i in s:
                if(0>i>255):
                    return 'Neither'
            
            return 'IPv4'
        
        elif(':' in IP):
            
            s = IP.split(':')
            
            for i in s:
                if()
            
            