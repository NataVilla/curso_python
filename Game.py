import random


def seleccion_opcion():
    print("Bienvenidos al juego de priedra, papel o tijera")
    
    opciones = ('piedra', 'papel', 'tijera')
    opcion_usurio = input('piedra, papel, tijera => ')
    
    opcion_usurio= opcion_usurio.lower()
    
    if not opcion_usurio in opciones:
        print('Esa opcion no es valida')
        
        return None, None
    
    opcion_pc = random.choice(opciones)
    
    print('opcion usuario => ', opcion_usurio)
    print('opcion pc => ', opcion_pc)
    
    return opcion_usurio, opcion_pc


def reglas(opcion_usurio, opcion_pc, gana_usuario, gana_pc):
    if opcion_usurio == opcion_pc:
        print('Empate')
    elif opcion_usurio == 'piedra':
        if opcion_pc == 'tijera':
            print('Piedra gana a tijera')
            print('Usuario gana')
            gana_usuario +=1
        else:
            print('papel gana a piedra')
            print('PC gana')
            gana_pc +=1
    elif opcion_usurio == 'papel':
        if opcion_pc == 'piedra':
            print('papel gana a piedra')
            print('Usuario gana')
            gana_usuario +=1
        else:
            print('Tijera gana a papel')
            print('PC gana')
            gana_pc +=1
    elif opcion_usurio == 'tijera':
        if opcion_pc == 'papel':
            print('Tijera gana a papel')
            print('Usuario gana')
            gana_usuario +=1
        else:
            print('Piedra gana a tijera')
            print('PC gana')
            gana_pc +=1       
            
    return gana_usuario, gana_pc        
        
def run_game():
    gana_pc = 0
    gana_usuario = 0        
    rounds = 1
    
    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)
        
        print('PC gana', gana_pc)
        print('Usuario gana', gana_usuario)
        rounds +=1
        
        opcion_usurio, opcion_pc = seleccion_opcion()
        gana_usuario, gana_pc = reglas(opcion_usurio, opcion_pc, gana_usuario, gana_pc)
        
        if gana_pc == 2:
            print('Gana la PC')
            break
        if gana_pc == 2:
            print('Gana usuario')
            break
        

run_game() 
        