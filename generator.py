
class read_configuration:
    def __init__(self, main_argv):
        self.SRV_USER = main_argv[1]
        self.ARCHIVE_URL = main_argv[2]
        self.INSTANCE_NAME = main_argv[3]
        self.GAME = main_argv[4]
        self.SRV_PORT = int(main_argv[5])
        self.SRV_NAME = main_argv[6]
        self.SRV_DESCRIPTION = main_argv[7]

        self.SRV_FILENAME = self.ARCHIVE_URL.split('/')[-1]
        self.SRV_HOME_PATH = "/home/" + self.SRV_USER
        self.SRV_PATH = self.SRV_HOME_PATH + "/" + self.INSTANCE_NAME
        self.to_install = "xxx"
        self.SETTINGS_FILE_NAME = {
            'KMR': "KaM Remake Server Settings.ini",
            'KP': "KnightsProvince_Settings.ini"
            }
        self.GAME_FULL_NAME = {
            'KMR': "KaM Remake",
            'KP': "Knights Province"
            }
        self.GAME_BINARY_NAME = {
            'KMR': "KaM_Remake_Server_linux_x86_64",
            'KP': "KP_DedicatedServer_Linux_x64"
            }
        self.SYSTEMD_ALL_UNITS_PATH = "/usr/lib/systemd/system"
        self.SYSTEMD_UNIT_NAME = self.GAME + "-" + self.INSTANCE_NAME + ".service"
        self.SYSTEMD_UNIT_PATH = self.SYSTEMD_ALL_UNITS_PATH + "/" + self.SYSTEMD_UNIT_NAME
        self.SYSTEMD_UNIT_CONTENT = '''[Unit]
Description=''' + self.GAME_FULL_NAME[self.GAME] + " " + self.INSTANCE_NAME + ''' game server
After=network.target

[Service]
WorkingDirectory=''' + self.SRV_PATH + '''
User=''' + self.SRV_USER + '''
Group=''' + self.SRV_USER + '''
Type=simple
ExecStart=''' + self.SRV_PATH + "/" + self.GAME_BINARY_NAME[self.GAME] + '''
RestartSec=15
Restart=always

[Install]
WantedBy=multi-user.target'''

    def sed_ini(self, key, value):
        print('sed -i "s/' + key + '=.*/' + key + '=' + value + '/g" "' + self.SETTINGS_FILE_NAME[self.GAME] + '"')

        '''
ServerName='REPLACE_SERVER_NAME'
WelcomeMessage=REPLACE_WELCOME_MESSAGE
ServerPort=REPLACE_SERVER_PORT
UDPScanPort=REPLACE_SERVER_PORT_2
        '''

    def generate_instructions(self):
        # print("apt update\napt install " + self.to_install)
        print("useradd " + self.SRV_USER + " -m " + self.SRV_HOME_PATH )
        print("mkdir -p " + self.SRV_PATH)
        print("curl -L " + self.ARCHIVE_URL + " -o " + self.SRV_PATH + "/" + self.SRV_FILENAME)
        print("cd " + self.SRV_PATH )
        print("7z x " + self.SRV_FILENAME  + " " + self.SRV_PATH)
        print("chmod +x " + self.GAME_BINARY_NAME[self.GAME])
        print("echo '" + self.SYSTEMD_UNIT_CONTENT  + "' > " + self.SYSTEMD_UNIT_PATH + "\n\nchmod +x " + self.SYSTEMD_UNIT_PATH + "\n")
        print("systemctl start " + self.SYSTEMD_UNIT_NAME + "; sleep 3; systemctl stop " + self.SYSTEMD_UNIT_NAME)
        self.sed_ini("ServerName", '\'' + self.SRV_NAME + '\'')
        self.sed_ini("WelcomeMessage", self.SRV_DESCRIPTION)
        self.sed_ini("ServerPort", str(self.SRV_PORT))
        if self.GAME == 'KMR':
            self.sed_ini("UDPScanPort", str(self.SRV_PORT + 1))

'''
TODO
- start server, sleep 5, stop server, replace INI settings, start server

optional:
- check if port is already used
'''
