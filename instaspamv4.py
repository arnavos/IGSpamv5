from libs.check_modules import check_modules
from sys import exit
from os import _exit

check_modules()

from os import path

from libs.logo import print_logo
from libs.utils import print_success
from libs.utils import print_error
from libs.utils import ask_question
from libs.utils import print_status
from libs.utils import parse_proxy_file
from libs.proxy_harvester import find_proxies
from libs.attack import report_profile_attack
from libs.attack import report_video_attack

from multiprocessing import Process
from colorama import Fore, Back, Style

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def profile_attack_process(username, proxy_list):
    if len(proxy_list) == 0:
        for _ in range(10):
            report_profile_attack(username, None)
        return

    for proxy in proxy_list:
        report_profile_attack(username, proxy)

def video_attack_process(video_url, proxy_list):
    if len(proxy_list) == 0:
        for _ in range(10):
            report_video_attack(video_url, None)
        return

    for proxy in proxy_list:
        report_video_attack(video_url, proxy)

def video_attack(proxies):
    video_url = ask_question("Please enter the URL of the video you want to report")
    print(Style.RESET_ALL)
    if len(proxies) == 0:
        for k in range(5):
            p = Process(target=video_attack_process, args=(video_url, [],))
            p.start()
            print_status(str(k + 1) + ". Process Started!")
            if k == 5: print()
        return

    chunk = list(chunks(proxies, 10))

    print("")
    print_status("Starting video report attack!\n")

    i = 1
    for proxy_list in chunk:
        p = Process(target=video_attack_process, args=(video_url, proxy_list,))
        p.start()
        print_status(str(i) + ". Process Started!")
        if i == 5: print()
        i += 1

def profile_attack(proxies):
    username = ask_question("Please enter the username of the person you want to report")
    print(Style.RESET_ALL)
    if len(proxies) == 0:
        for k in range(5):
            p = Process(target=profile_attack_process, args=(username, [],))
            p.start()
            print_status(str(k + 1) + ". Process Started!")
        return

    chunk = list(chunks(proxies, 10))

    print("")
    print_status("Starting profile report attack!\n")

    i = 1
    for proxy_list in chunk:
        p = Process(target=profile_attack_process, args=(username, proxy_list,))
        p.start()
        print_status(str(i) + ". Process Started!")
        if i == 5: print()
        i += 1

def main():
    while True:
        print_success("Modules loaded!\n")

        ret = ask_question("Would you like to use proxies? [Y/N]")

        proxies = []

        if ret.lower() == "y":
            ret = ask_question("Would you like to gather proxies from the internet? [Y/N]")

            if ret.lower() == "y":
                print_status("Gathering proxies from the internet! This may take a while.\n")
                proxies = find_proxies()
            elif ret.lower() == "n":
                print_status("Please ensure no more than 50 proxies per file!")
                file_path = ask_question("Please enter the path to your proxy list")
                proxies = parse_proxy_file(file_path)
            else:
                print_error("Answer not understood, exiting!")
                exit()

            print_success(f"{len(proxies)} proxies found!\n")
        elif ret.lower() == "n":
            pass
        else:
            print_error("Answer not understood, exiting!")
            exit()

        print("")
        print_status("1 - Report a profile.")
        print_status("2 - Report a video.")
        report_choice = ask_question("Please select the reporting method")
        print("")

        if not report_choice.isdigit():
            print_error("Answer not understood.")
            continue

        if int(report_choice) > 2 or int(report_choice) == 0:
            print_error("Answer not understood.")
            continue

        if int(report_choice) == 1:
            profile_attack(proxies)
        elif int(report_choice) == 2:
            video_attack(proxies)

        another_round = ask_question("Would you like to perform another operation? [Y/N]")
        if another_round.lower() != "y":
            break

if __name__ == "__main__":
    print_logo()
    try:
        main()
        print(Style.RESET_ALL)
    except KeyboardInterrupt:
        print("\n\n" + Fore.RED + "[ * ] Program is shutting down!")
        print(Style.RESET_ALL)
        _exit(0)