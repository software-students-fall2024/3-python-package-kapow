import os

def askAnimal():
    while(True):
        os.system('clear');
        animal = '''
                            __________________________________
                            |    Ribbet! What do you want?   |
                            ----------------------------------
                              / /
                             / /
                _         _ / /
    __   ___.--'_`.     .'_`--.___   __
    ( _`.'. -   'o` )   ( 'o`   - .`.'_ )
    _\.'_'      _.-'     `-._      `_`./_
    ( \`. )    //\`         '/\\    ( .'/ )
    \_`-'`---'\\__,       ,__//`---'`-'_/
    \`        `-\         /-'        '/
    `                               '   
    '''
        print(animal);
        menuInput = input("I want to (CONVERT/COMPARE): ")
        print(menuInput);
        menuInput = input("Continue? (Y/N): ")
        if(menuInput == "N"):
            break

askAnimal();