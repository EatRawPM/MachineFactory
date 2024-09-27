from src.data.path import main_path
from os.path import join, exists
from os import mkdir

from src.data.game.settings.create import create_settings

data_path = join(main_path, 'MachineFactory')

settings_path = join(data_path, 'settings.json')

def data_init():
    def main_data():
        def data():
            def settings():
                if exists(settings_path):
                    print(f'{settings_path} already exists')
                else:
                    with open(settings_path, 'w') as f:
                        create_settings(f)
                    print(f'{settings_path} created!')

            if exists(data_path):
                print(f'{data_path} already exists')
                settings()
            else:
                mkdir(data_path)
                print(f'{data_path} created!')
                settings()

        if exists(main_path):
            print(f'{main_path} already exists')
            data()
        else:
            mkdir(main_path)
            print(f'{main_path} created!')
            data()

    main_data()