class Phone:

    def __init__(self, access):
        self._access = access

        
    def get_status(self):
        '''
        Get phone status:
        '''
        return self._access.get('phone/')


    def get_config(self):
        '''
        Get phone configuration:
        '''
        return self._access.get('phone/config/')


    def set_config(self, conf):
        '''
        Update phone configuration:
        '''
        self._access.put('phone/config/', conf)


    def get_dect_vendors(self):
        '''
        Get phone configuration:
        '''
        return self._access.get('phone/dect_vendors/')

