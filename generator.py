
class read_configuration:
    def __init__(self, USERNAME, KMR_URL, SRV_NAME):
        self.USERNAME = USERNAME
        self.KMR_URL = KMR_URL
        self.KMR_INSTANCE_NAME = SRV_NAME
        self.to_install = "xxx"


    def generate_instructions(self):
        print("apt update\napt install " + self.to_install)
        systemd_unit = '''file
content
here'''
        print("[MANUAL] xxx")
