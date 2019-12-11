#created by azad
#follow me on IG @p8z4
#FKnoobs V1.0
import socket 

# def azad : bashek bo away codeakani tya bnusin
def azad():
    # aza = socket.socket(..... farman krd u re pekan bo hanek shti socketaka
    aza = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('''
        
        ███████╗       ██████╗██╗  ██╗    ███╗   ██╗ ██████╗  ██████╗ ██████╗ ███████╗
        ██╔════╝▄ ██╗▄██╔════╝██║ ██╔╝    ████╗  ██║██╔═══██╗██╔═══██╗██╔══██╗██╔════╝
        █████╗   ████╗██║     █████╔╝     ██╔██╗ ██║██║   ██║██║   ██║██████╔╝███████╗
        ██╔══╝  ▀╚██╔▀██║     ██╔═██╗     ██║╚██╗██║██║   ██║██║   ██║██╔══██╗╚════██║
        ██║       ╚═╝ ╚██████╗██║  ██╗    ██║ ╚████║╚██████╔╝╚██████╔╝██████╔╝███████║
        ╚═╝            ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝
        with azad V 1.0 #know_a_little_about_everything
        ''')
    ip = input(' [!] ip chanda : ')
    print(' =-=-=-=-=-=-=-=-=-=-=-=-=')
    port = int(input(' [!] port chanda : '))
    print(' =-=-=-=-=-=-=-=-=-=-=-=-=')
    
    print(' [!] lasar aw hosta karaya : ' + (ip))
    # lera ip u port ba yakawa bind akain
    aza.bind((ip,port))
    # bo listen krdni ip u portaka
    aza.listen(5)
    while True:
        xd, aza1 = aza.accept() # lere bo qbull krdni ip u portaka
        print(' =-=-=-=-=-=-=-=-=-=-=-=-=')
        print(" [!] lasar awa krayawa : " + str(aza1))
        xd.close()

if __name__ == '__main__':
    azad()