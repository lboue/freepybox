class Lcd:

    def __init__(self, access):
        self._access = access


    def get_config(self):
        '''
        Get wifi LCD configuration:
        '''
        return self._access.get('lcd/config/')


    def set_config(self, conf):
        '''
        Update LCD configuration:
        '''
        self._access.put('lcd/config/', conf)
 
