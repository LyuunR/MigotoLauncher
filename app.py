import subprocess, json, time, os, shutil

print("[MigotoLauncher] Starting Up...")
defaultConfig = {"GenshinPath": "?", "MigotoPath": "?"}
if os.path.isfile("./config.json"):
    print("[MigotoLauncher] Config file exists, Skipping creation...")
else:
    configInit = json.dumps(defaultConfig, indent=2)
    with open("config.json", "w") as cfg:
        cfg.write(configInit)
    print("[MigotoLauncher] Newly initalized. First time setup may be required!")

ConfigFile = open('config.json')
ConfigData = json.load(ConfigFile)
print("[MigotoLauncher] Loaded Data.")
print("[MigotoLauncher] If you see the 3dMigoto window feel free to close this one!")
def Main(mp, gp):
    shutil.copyfile(mp+"/d3dx.ini", os.getcwd()+"/d3dx.ini")
    subprocess.run(mp+"/3dMigoto.exe", shell=False)
    time.sleep(3)
    subprocess.run(gp+"/GenshinImpact.exe", shell=True)

GenshinPath = ConfigData['GenshinPath']
MigotoPath = ConfigData['MigotoPath']
if MigotoPath == "?":
    migotoPath = input("[MigotoLauncher] Enter the path to 3dMigoto's directory, Do not include the executable: ")
    r = migotoPath.replace("\\", "/")
    ConfigData["MigotoPath"] = r
    with open('config.json', 'r+') as e:
        json.dump(ConfigData, e, indent=2)
if GenshinPath == "?":
    genshinPath = input("[MigotoLauncher] Enter the path to Genshin Impact Game directory:  ")
    s = genshinPath.replace("\\", "/")
    ConfigData["GenshinPath"] = s
    with open('config.json', 'r+') as e:
        json.dump(ConfigData, e, indent=2)
    Main(r, s)
else: 
    Main(MigotoPath, GenshinPath)
