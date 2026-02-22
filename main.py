#!/usr/bin/env python
# import subprocess
import sys
import generator

if len(sys.argv) < 4:
    print("Error - you need 3 arguments and this is what you provided: " + str(sys.argv[1:]))
    print("SRV_USER which will run the server")
    print("ARCHIVE_URL to dedicated server archive")
    print("INSTANCE_NAME - name for server directory/service ie. kp_r12345 - you can deploy multiple versions that way")
    print("GAME - KMR or KP")
    exit(1)
else:
    c1 = generator.read_configuration(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    c1.generate_instructions()
    print("Done.")
