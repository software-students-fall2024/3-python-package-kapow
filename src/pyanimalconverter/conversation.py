import os
from pint import UnitRegistry

ureg = UnitRegistry()
Q_ = ureg.Quantity

def talk(rightText="",leftText=""):
    one_speechBubbleTop = '''
                                            ----------------------------------
    '''
    one_speechBubbleBottom = '''
                                            ---   _---------------------------
                                              / _/
                                             //
    '''
    middleText = f'''
              {leftText}                                   {rightText}
    '''
    both_speechBubbleTop = '''
        -----------------------------       ----------------------------------
    '''
    both_speechBubbleBottom = '''
        ----_   ---------------------       ---   _---------------------------
            \ _\                              / _/
                \\                           //
    '''
    animal = '''
                        _           _ 
            __   ___.--'_`.       .'_`--.___   __
            ( _`.'. -   'o` )     ( 'o`   - .`.'_ )
            _\.'_'      _.-'       `-._      `_`./_
            ( \`. )    //\`           '/\\    ( .'/ )
             \_`-'`---'\\__,         ,__//`---'`-'_/
              \`        `-\           /-'        '/
               `                                 '   
    '''
    if(leftText==""):
        return one_speechBubbleTop + middleText + one_speechBubbleBottom + animal
    else:
        return both_speechBubbleTop + middleText + both_speechBubbleBottom + animal

def askAnimal():
    navigation = "menu";
    while(True):
        os.system('clear');
        if(navigation=="menu"):
            print(talk("Ribbit, what do you want?"))
            menuInput = input("I want to (CONVERT/COMPARE) some numbers: ")
            print(menuInput);
            if(menuInput=="CONVERT"):
                navigation="convert";
        if(navigation=="convert"):
            os.system('clear');
            print(talk("Ribbit, ok, what number do you want to convert?","I want to convert a number!"));
            validUnit = True;
            while(True):
                convertFrom = input("Enter the number with units (e.g. 1 kg, 5 kg) you want to convert: ");
                try:
                    convertFrom_num = Q_(convertFrom);
                except Exception as e:
                    print(e);
                else:
                    os.system('clear');
                    convertTo = input("")
        menuInput = input("Continue? (Y/N): ")
        if(menuInput == "N"):
            break

askAnimal();