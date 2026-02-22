
class read_configuration:
    def __init__(self, main_argv):
        self.SRV_USER = main_argv[1]
        self.ARCHIVE_URL = main_argv[2]
        self.INSTANCE_NAME = main_argv[3]
        self.GAME = main_argv[4]
        self.SRV_PORT = int(main_argv[5])
        self.SRV_NAME = "\$".join(main_argv[6].split('$'))
        #str([print(part + '\$') for part in main_argv[6].split('$')])
        self.SRV_DESCRIPTION = "\$".join(main_argv[7].split('$'))

        self.SRV_FILENAME = self.ARCHIVE_URL.split('/')[-1]
        self.SRV_HOME_PATH = "/home/" + self.SRV_USER
        self.SRV_PATH = self.SRV_HOME_PATH + "/" + self.INSTANCE_NAME
        self.to_install = "p7zip-full"
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

    def generate_instructions(self):
        print("apt update\napt install " + self.to_install)
        print("useradd -m -d " + self.SRV_HOME_PATH + " " + self.SRV_USER )
        print("mkdir -p " + self.SRV_PATH)
        print("cd " + self.SRV_PATH )
        print("curl -L " + self.ARCHIVE_URL + " -o " + self.SRV_FILENAME)
        print("7z x " + self.SRV_FILENAME)
        print("chmod +x " + self.GAME_BINARY_NAME[self.GAME])
        print("chown " + self.SRV_USER + ":" + self.SRV_USER + " -R " + self.SRV_PATH)
        print("echo '" + self.SYSTEMD_UNIT_CONTENT  + "' > " + self.SYSTEMD_UNIT_PATH + "\n\nchmod +x " + self.SYSTEMD_UNIT_PATH + "\n")
        print("systemctl start " + self.SYSTEMD_UNIT_NAME + "; sleep 3; systemctl stop " + self.SYSTEMD_UNIT_NAME)
        self.sed_ini("ServerName", '\'' + self.SRV_NAME + '\'')
        self.sed_ini("WelcomeMessage", self.SRV_DESCRIPTION)
        self.sed_ini("ServerPort", str(self.SRV_PORT))
        if self.GAME == 'KMR':
            self.sed_ini("UDPScanPort", str(self.SRV_PORT + 1))
        print("rm " + self.SRV_FILENAME)

'''
TODO

optional:
- check if port is already used
'''
