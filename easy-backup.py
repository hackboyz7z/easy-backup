
#print '''
print("                                  X8xXS8X                         ")
print("             .  . .  .  . .  . .;88XX@XSSSX8% . .  . .  . .  . .  ")
print("             .       .       .@@@@8S;;%S8SXS8.        .    .    . ")
print("               .  .    .  .  S@@@S  .  ..XSSSX  . .      .    .   ")
print("           .       .       ..8X@8.       .8%S8:     .  .    .     ")
print("             .  .    .  .   :8X8@  .  .  .XSSX:  .   .    .    .  ")
print("             .    .  .    .  :8ZXS    .    XSS@:    .    .    .   ")
print("              .       .     :8S8@ .    .  XSS@:  .    .   .    .  ")
print("            .   . .    .  .XS%S:S8X8@XX;X;S  S:8.   .   .   .     ")
print("              .     .    .@ 88@@@S@X@@8@888888@88.        .   .   ")
print("            .    .   .    @@88888888@ 8888X888888: .  .     .   . ")
print("               .   .   .  8X888 @8X8   :88888X@88%      .         ")
print("            .    .      . 8X88888888   88X8888888t . .    .  . .  ")
print("              .     . .  .88888888888.888@X8 8888;    .    .      ")
print("            .   .        :8888888S888%@8888888@88S  .   .    .  . ")
print("              .   . .  . :8X8888888888@888%888888t     .   .      ")
print("            .            .t88888888888@8S88 8888X::  .        .   ")

print("                                     ___.                  __                  ")
print("  ____ _____    _________.__.        \_ |__ _____    ____ |  | ____ ________  ")
print("_/ __ \\__  \  /  ___<   |  |  ______ | __ \\__  \ _/ ___\|  |/ /  |  \____ \ ")
print("\  ___/ / __ \_\___ \ \___  | /_____/ | \_\ \/ __ \\  \___|    <|  |  /  |_> >")
print(" \___  >____  /____  >/ ____|         |___  (____  /\___  >__|_ \____/|   __/ ")
print("     \/     \/     \/ \/                  \/     \/     \/     \/     |__|    ")

print("script orientado a automatizar tareas a los administradores\n de sistemas linux")
print("|----------------------------------------------------------------------------------|")

import os
from datetime import date
from datetime import datetime
from datetime import time
from colorama import init, Fore, Back, Style

print(Fore.BLUE + "(1)-Informacion del sistema")
print("(2)-Realizar backups")
print("(3)-Gestionar usuarios")
print("(4)- abortar mision")

opcion = input()


if opcion == "1":

    os.system("clear")

    print(" ____                                                              ")
    print(" \\  `.                                                            ")
    print("  \\   `.                                                          ")
    print("   \ \   `.                                                        ")
    print("    \\01838`.                                                      ")
    print("    :. . . . `._______________________.-~|~~-._                    ")
    print("    \                                 ---'-----`-._                ")
    print("     /++++++|             _...---------..         ~-._________    ")
    print("    //     .`_________  .-`           \ .-~           /            ")
    print("   //    .'       ||__.~             .-~_____________/             ")
    print("  //___.`           .~            .-~                              ")
    print("                  .~           .-~                                 ")
    print("                .~         _.-~                                    ")
    print("                `-_____.-~'                                        ")

    print("(1)-arquitectura de la maquina")
    print("(2)-version del quernel")
    print("(3)-arquitectura de la maquina")
    print("(4)- mostrar dispositivos conectados")
   
    
    info = input()
    if info == "1":
        os.system("uname -m") #arquitectura de la maquina
        
    elif info == "2":
        os.system("uname -r") #version del quernel usado
        
    elif info == "3": 
        os.system("dmidecode -q") #hardware del sistema
    
    elif info == 4:
        os.system("lsblk")
        
    else:
        print("opcion no valida.....saliendo del script")
        os.system("python3 samurai.py")

#=========================================================    
elif opcion == "2":
    os.system("clear")

    print("MMMMMMMMMMMMMMWWNXOxxOXNXXWMMMMMMMMMMMMM")
    print("MMMMMMMMMMWNK0OO0KKdc:lkxd0WWMMMMMMMMMMM")
    print("MMMMMMMMMMWXOdl::cl:;;;;;:dOKMMMMMMMMMMM")
    print("MMMMMMMMMMWX0kl;'''''''',;:ckNMMMMMMMMMM")
    print("MMMMMMMMMWNKOxddol;'.'cxO000KNWMMMMMMMMM")
    print("MMMMMMMMMWNXKNWMMW0o:dXMMMMMWNNWMMMMMMMM")
    print("MMMMMMMWKKWWW0kKMMNXK0k0WMMMMWXKXMMMMMMM")
    print("MMMMMMWx,lNMWxcOWWXK0kcdNMMMMWKcc0MMMMMM")
    print("MMMMMNd. .c0NWWWNK0000KNWMMWXk:..;0MMMMM")
    print("MMMNO:.    .,:cldkkkkxl;;cc;'   . ,OWMMM")
    print("MNO;.           .'''..          .  .:OWM")
    print("0c.                                  .lK")
    print(",....         'coxOOOOkxoc'.          .,")
    print("OOKKl      .cOXWWWWWWWWWWWXOc.   ...lOkk")
    print("MMMWx.    'kNWWNWWWWNWWWWWWWNk,  ..'kMMM")
    print("MMMMK;   .dNNNNNNNNNNNNNNNNNNNx. ..cXMMM")
    print("MMMMWO'  .dKKKXXXXXXXXXXXXXKKKo. .:0MMMM")
    print("MMMMMW0c;:d00O0KXXXXXXXXXK0O00d::oKWMMMM")
    print("MMMMMMWXOOOOOOkO0KKKKKKK0kkOOOOOOXWMMMMM")
    print("MMMMMMN0kxkkkkxo;,;;;;;,:oxkxkkxk0NMMMMM")
    print("MMMMMMWXK00OOkkdl:::;::coxOOOO00KXWMMMMM")
    print("MMMMMMMMMMMMWWWNNXXXXXXNNWWWWWWMMMMMMMMM")

    print("(1)-gestionar backups")
    print("(2)-ver reporte de respaldos")

    
    back = input()
    
    if back == "1":
        os.system("clear")

        print("(a-Reslpaldar Documentos)")
        print("(b-Reslpaldar Descargas)")
        print("(c-Reslpaldar Imagenes)")
        print("(d-Reslpaldar Videos)")
        print("(|--------------------------------------|)")
        print("(e-Reslpaldar Usuario)")
        
        respal = input()
        if respal == "a":
            #realizando el backup
            print("generando respaldo carpeta Documentos, espere...")
            os.system("cp -r /home/samuraimx/Documentos /home")
            print("respaldo finalizado...")

            #archivo bitacora
            if os.path.exists("backup.txt")== True:
                print("existe")
            
            else:
                print("no existe")

            hoy = datetime.now()
            fecha = hoy.strftime("%d/%m/%Y")
            hora = hoy.strftime("%I:%M:%S")

            fichero = open("backups.txt", "a+")
            fichero.write("\n" + fecha + " " + hora)
            fichero.close()
            os.system("python3 samurai.py")

        elif respal == "b":
            #realizando el backup
            print("generando respaldo carpeta Descargas, espere...")
            os.system("cp -r /home/samuraimx/Descargas /home")
            print("respaldo finalizado...")

            #archivo bitacora
            if os.path.exists("backup.txt")== True:
                print("existe")
            
            else:
                print("no existe")

            hoy = datetime.now()
            fecha = hoy.strftime("%d/%m/%Y")
            hora = hoy.strftime("%I:%M:%S")

            fichero = open("backups.txt", "a+")
            fichero.write("\n" + fecha + " " + hora)
            fichero.close()
            os.system("python3 samurai.py")
    
        elif respal == "c":
            #realizando el backup
            print("generando respaldo carpeta Imágenes, espere...")
            os.system("cp -r /home/samuraimx/Imágenes /media/samuraimx/Windows")
            print("respaldo finalizado...")

            #archivo bitacora
            if os.path.exists("backup.txt")== True:
                print("existe")
            
            else:
                print("no existe")

            hoy = datetime.now()
            fecha = hoy.strftime("%d/%m/%Y")
            hora = hoy.strftime("%I:%M:%S")

            fichero = open("backups.txt", "a+")
            fichero.write("\n" + fecha + " " + hora)
            fichero.close()
            os.system("python3 samurai.py")


        elif respal == "d":
            #realizando el backup
            print("generando respaldo carpeta Videos, espere...")
            os.system("cp -r /home/samuraimx/Vídeos /home")
            print("respaldo finalizado...")

            #archivo bitacora
            if os.path.exists("backup.txt")== True:
                print("existe")
            
            else:
                print("no existe")

            hoy = datetime.now()
            fecha = hoy.strftime("%d/%m/%Y")
            hora = hoy.strftime("%I:%M:%S")

            fichero = open("backups.txt", "a+")
            fichero.write("\n" + fecha + " " + hora)
            fichero.close()
            os.system("python3 samurai.py")


        elif respal == "e":
            #realizando el backup
            print("generando respaldo, espere...")
            os.system("cp -r /home/samuraimx /home")
            print("respaldo finalizado...")

            #archivo bitacora
            if os.path.exists("backup.txt")== True:
                print("existe")
            
            else:
                print("no existe")

            hoy = datetime.now()
            fecha = hoy.strftime("%d/%m/%Y")
            hora = hoy.strftime("%I:%M:%S")

            fichero = open("backups.txt", "a+")
            fichero.write("\n" + fecha + " " + hora)
            fichero.close()
            os.system("python3 samurai.py")


    elif back == "2":
        print("consultando reportes")
        #fichero = open("backups.txt", "r")
        os.system("gedit backups.txt")

    else:
        print("opcion invalida")

        os.system("python3 samurai.py")

#====================================================================


elif opcion == "3":
    os.system("clear")

    print("             .@ X%88@S :8@:..            ")
    print("  .  . .  :X@:@888888888@@X S. .  . .  .")
    print("   .     @:88X88@88S888X88888:8.        ")
    print("     .  8S8X88S@X888@@X88888X8XX .  . . ")
    print(" .     ;S8888X@@@8888@X888888888.       ")
    print("   .  .X8@8X8@XS8Xt S;88888@8@8%@.  .  .")
    print("  .    S8X8@X:; 88.XSXSSSS88S8@8X       ")
    print("    .  t@8XS 88S8:8 8 88%.8@8X88S.  . . ")
    print("  .   .Xt.;8X S@X 8888@SX  S8;X.% .     ")
    print("    .  .88S8 8S@@@ 88888888SXt888.     .")
    print("  .    :@8888 88  88888 S 8 888%@   .   ")
    print("     .  S88888888888888 8 888888t .     ")
    print("  .     .%:88888888888888@88888;     .  ")
    print("    . .  .t88888888888 8 8888S.  .  .   ")
    print("  .     . .%888888888888888@%         . ")
    print("    .    .  ;S8888888S@88X8: . .  .     ")
    print("  .   .    . ::888888888%:..        .   ")
    print("       .    ..:X 8888888X;.   .  .    . ")
    print("  . .    ..t%888t 8 8S8SS@8 S      .    ")
    print("       .18X:8X8.@;22  S@ :@ 88S%     .  ")
    print("  .  .X@:8X.@ 8..88@88.;8;;8.8@X@8      ")
    print("    .8.88 8X 8;8X  @8.8X.8@888@ X :     ")
    print("  ..8 88888@;8.88.8 8:@888@X88:88888:   ")
    print("   8 88X.:8:8 8X8888 8X88.:8:t8 88@.%   ")


    print("gestionando usuarios del sistema\n")
    print("(1)-listando usuarios alfabeticamente")
    
    usu = input("selecciona opcion")
    
    

    if usu == "1":
        
        os.system("cut -d: -f1 /etc/passwd | sort")


elif opcion == "4":
    print("saliendo finalizando easy-backup")
    
    abortar=input()
    if abortar == "4":
        os.system("ctr + c")
        os.system("ctr + c")
        os.system("clear")


else:
    print("opcion no valida.....saliendo del script")
    os.system("python3 samurai.py")