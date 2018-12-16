#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This example can be run safely as it won't change anything in your box configuration
'''
import pprint
from freepybox import Freepybox

# Instantiate Freepybox class using default application descriptor 
# and default token_file location
fbx = Freepybox()
pp = pprint.PrettyPrinter(indent=4)

# Connect to the freebox with default http protocol
# and default port 80
# Be ready to authorize the application on the Freebox if you use this
# example for the first time
fbx.open('mafreebox.freebox.fr', 80)

# Extract VPN status (GET /api/v6/vpn) using connection API
print('### VPN ###')
fbx_vpn_status = fbx.vpn.get_status()
print(fbx_vpn_status)
pp.pprint(fbx_vpn_status)

# VPN users
fbx_vpn_users = fbx.vpn.get_users()
print('VPN users: {0}'.format(fbx_vpn_users))
pp.pprint(fbx_vpn_users)

# POST /api/v6/vpn/user
fbx_vpn_new_user = fbx.vpn.set_users()
print('VPN new user: {0}'.format(fbx_vpn_new_user))

# DELETE /api/v6/vpn/user/test
fbx.vpn.delete_user("username")

# VPN connection list
fbx_vpn_connection = fbx.vpn.get_connection()
print(fbx_vpn_connection)

# VPN IPSEC config
fbx_vpn_ipsec_config = fbx.vpn.get_ipsec_config()
print('VPN IPSEC config: {0}'.format(fbx_vpn_ipsec_config))
pp.pprint(fbx_vpn_ipsec_config)

print('\n')

# VPN PPTP config
fbx_vpn_pptp_config = fbx.vpn.get_pptp_config()
print('VPN PPTP config: {0}'.format(fbx_vpn_pptp_config))
pp.pprint(fbx_vpn_pptp_config)

# Close the freebox session
fbx.close()
