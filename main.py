import requests, time, os, sys, pystyle, time

def main():

    def deco():

        ascii = '''
        
        █████▒ ▐██▌  ▄████▄   ██ ▄█▀
        ▓██   ▒  ▐██▌ ▒██▀ ▀█   ██▄█▒
        ▒████ ░  ▐██▌ ▒▓█    ▄ ▓███▄░
        ░▓█▒  ░  ▓██▒ ▒▓▓▄ ▄██▒▓██ █▄
        ░▒█░     ▒▄▄  ▒ ▓███▀ ░▒██▒ █▄
        ▒ ░     ░▀▀▒ ░ ░▒ ▒  ░▒ ▒▒ ▓▒
        ░       ░  ░   ░  ▒   ░ ░▒ ▒░
        ░ ░        ░ ░        ░ ░░ ░
                ░    ░ ░      ░  ░
                    ░
        '''

        pystyle.System.Size(150, 50)

        pystyle.System.Title('K1ng')

        pystyle.Anime.Fade(pystyle.Center.Center(ascii), pystyle.Colors.red_to_blue, pystyle.Colorate.Vertical, enter=True)

    deco()

    def interpreter():

        Cells = [0, 0, 0, 0]

        Pointer = 0

        Command = pystyle.Write.Input("Command > ", pystyle.Colors.red_to_blue)

        for c in Command:

            if c == ">":

                if Pointer == 0:
                    Pointer = 1
                    
                elif Pointer == 1:
                    Pointer = 2
                    
                elif Pointer == 2:
                    Pointer = 3
                    
                elif Pointer == 3:
                    print("Error")

            elif c == "<":

                if Pointer == 0:
                    print("Error")

                elif Pointer == 1:
                    Pointer = 0
                    
                elif Pointer == 2:
                    Pointer = 1
                    
                elif Pointer == 3:
                    Pointer = 2
                    
            elif c == "+":
                Cells[Pointer] = Cells[Pointer] + 1
                
            elif c == "-":
                Cells[Pointer] = Cells[Pointer] - 1
                
            elif c == ".":
                print(str(Cells[Pointer]))
            
            elif c == ",":
                Entry = input("Input > ")
                Cells[Pointer] = int(Entry)
        
        print()

        os.system('pause')
                
    interpreter()

main()