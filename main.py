#!/usr/bin/env python
# import subprocess
import sys
import generator

if len(sys.argv) < 3:
    print("Error - you need 3 arguments and this is what you provided: " + str(sys.argv[1:]))
    print("username")
    print("KMR URL")
    print("SRV_NAME")
    exit(1)
else:
    c1 = generator.read_configuration(sys.argv[1], sys.argv[2], sys.argv[3])
    c1.generate_instructions()
    print("Done.")
