#!/usr/bin/env python
# import subprocess
import sys
import generator

ARGS_NR = 7

if len(sys.argv) < ARGS_NR + 1:
    print("Error - you need " + str(ARGS_NR) + " arguments and this is what you provided: " + str(sys.argv[1:]))
    print("SRV_USER which will run the server")
    print("ARCHIVE_URL to dedicated server archive")
    print("INSTANCE_NAME - name for server directory/service ie. kp_r12345 - you can deploy multiple versions that way")
    print("GAME - KMR or KP")
    print("SRV_PORT - ie. default 56789")
    print("SRV_NAME*")
    print("SRV_DESCRIPTION*")
    print("* - multi-word arguments - use ' ' around them (\" \" will not work well with color codes!)")
    exit(1)
else:
    print()
    c1 = generator.read_configuration(sys.argv)
    c1.generate_instructions()
    print("\n# Done. Now test connectivity and remember to allow access to your port on firewalls.")
