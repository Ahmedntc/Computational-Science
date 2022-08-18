import convert

print("\n   _____ ____  _   _ ________      ________ _____   _____  ____  _____    _____  ______   __  __ ______ _____ _____ _____           _____ ")
print("\n  / ____/ __ \| \ | |  ____\ \    / /  ____|  __ \ / ____|/ __ \|  __ \  |  __ \|  ____| |  \/  |  ____|  __ \_   _|  __ \   /\    / ____|   ")
print("\n | |   | |  | |  \| | |__   \ \  / /| |__  | |__) | (___ | |  | | |__) | | |  | | |__    | \  / | |__  | |  | || | | |  | | /  \  | (___     ")
print("\n | |   | |  | | . ` |  __|   \ \/ / |  __| |  _  / \___ \| |  | |  _  /  | |  | |  __|   | |\/| |  __| | |  | || | | |  | |/ /\ \  \___ \    ")
print("\n | |___| |__| | |\  | |____   \  /  | |____| | \ \ ____) | |__| | | \ \  | |__| | |____  | |  | | |____| |__| || |_| |__| / ____ \ ____) |   ")
print("\n  \_____\____/|_| \_|______|   \/   |______|_|  \_\_____/ \____/|_|  \_\ |_____/|______| |_|  |_|______|_____/_____|_____/_/    \_\_____/    ")


print("\nMENU\n")
print("1-Converter para metros")
print("2-converter para pés")
print("0- sair")
escolha = input("\nSua escolha: ")
valor = float(input("\n\nDigite o valor a ser convertido: "))

match escolha:
    case '1':
        valor = convert.pes_para_metros(valor)
        print("\nEm metros: %f metros" % valor)
    case '2':
        valor = convert.metros_para_pes(valor)
        print("\nEm pes: %f pés" % valor)
    case '0':
        exit()
    case other:
        print("\nComando não reconhecido!")
        exit()
            
        
        