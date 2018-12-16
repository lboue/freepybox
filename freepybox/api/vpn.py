class Vpn:

    def __init__(self, access):
        self._access = access


    def get_status(self):
        '''
        Get VPN status
        '''
        return self._access.get('vpn/')

    def get_ipsec_config(self):
        '''
        Get IPSEC VPN config
        '''
        return self._access.get('vpn/ipsec/config')

    def get_pptp_config(self):
        '''
        Get PPTP VPN config
        '''
        return self._access.get('vpn/pptp/config/')

    def get_openvpn_routed_config(self):
        '''
        Get OpenVPN routed VPN config
        '''
        return self._access.get('vpn/openvpn_routed/config')

    def get_openvpn_bridge_config(self):
        '''
        Get OpenVPN bridge VPN config
        '''
        return self._access.get('vpn/openvpn_bridge/config')

    def get_users(self):
        '''
        Get VPN users
        '''
        return self._access.get('vpn/user')

    def set_user(self):
        '''
        Get a new VPN user
        '''
        # JSON {"login":"username","password_set":false,"ip_reservation":"","password":"123456789"}
        data = {"login":"username","password_set":False,"ip_reservation":"","password":"123456789"}
        return self._access.post('vpn/user/', payload=data )

    def delete_user(self, user):
        '''
        Delete a VPN user
        '''
        URI = 'vpn/user/' +user
        return self._access.delete(URI)

    def get_connection(self):
        '''
        Get VPN connection list
        '''
        return self._access.get('vpn/connection')

