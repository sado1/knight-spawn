
class read_configuration:
    def __init__(self, SRV_USER, ARCHIVE_URL, SRV_NAME, GAME):
        self.SRV_USER = SRV_USER
        self.ARCHIVE_URL = ARCHIVE_URL
        self.INSTANCE_NAME = SRV_NAME
        self.GAME = GAME

        self.SRV_FILENAME = ARCHIVE_URL.split('/')[-1]
        self.SRV_HOME_PATH = "/home/" + self.SRV_USER
        self.SRV_PATH = self.SRV_HOME_PATH + "/" + self.INSTANCE_NAME
        self.to_install = "xxx"
        self.SETTINGS_FILE_NAME = {
            'KMR': "KaM Remake Server Settings.ini",
            'KP': "KnightsProvince_Settings.ini"
            }


    def generate_instructions(self):
        # print("apt update\napt install " + self.to_install)
        print("useradd " + self.SRV_USER + " -m " + self.SRV_HOME_PATH )
        print("mkdir -p " + self.SRV_PATH)
        print("curl -L " + self.ARCHIVE_URL + " -o " + self.SRV_PATH + "/" + self.SRV_FILENAME)
        print("cd " + self.SRV_PATH )
        print("7z x " + self.SRV_FILENAME  + " " + self.SRV_PATH)
        systemd_unit = '''file
content
here'''
        print("[MANUAL] xxx")
