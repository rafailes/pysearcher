from termcolor import colored
import requests
print(colored("""                                                .__     
______  __ __  ______ ____ _____ _______   ____ |  |__  
\____ \|  |  \/  ___// __ \\__  \\_  __ \_/ ___\|  |  \ 
|  |_> >  |  /\___ \\  ___/ / __ \|  | \/\  \___|   Y  \/
|   __/|____//____  >\___  >____  /__|    \___  >___|  /
|__|              \/     \/     \/            \/     \/ 

	@rafa_ailes_
	""", "green"))

url_target = input(colored("[*]𝐞𝐧𝐭𝐞𝐫 𝐭𝐚𝐫𝐠𝐞𝐭 𝐮𝐫𝐥 :  ", "green"))
directorie_wordlist = input(colored("[*]𝐞𝐧𝐭𝐞𝐫 𝐩𝐚𝐭𝐡𝐞 𝐭𝐨 𝐰𝐨𝐫𝐝𝐥𝐢𝐬𝐭 :   ", "green"))
test_requests = requests.get(url_target)
if test_requests.ok:
	print(colored(f"""
---------------------------------------------------------
target url : {url_target}

target statu : active

wordlist : {directorie_wordlist}                         
                                                        
---------------------------------------------------------
		""", "green"))

wordlist_opened = open(directorie_wordlist, "r")

for word in wordlist_opened:
	word = word.strip()
	directories = requests.get(f"{url_target}{word}")
	if directories.ok:
		print(colored(f"[*]one directorie found ! => {url_target}{word}", "green"))