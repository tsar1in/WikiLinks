import src.config as config
import src.logic as log


class Menu:
    def __init__(self):
        self.main = log.Logic()

    def LaunchMenu(self):
        while True:
            self.PrintMenu()
            tmp = int(input())
            if tmp == 0:
                break
            elif tmp == 1:
                self.main.SearchPath()
            elif tmp == 2:
                self.ChangeLanguage()
            elif tmp == 3:
                self.ChangeTarget()

    @staticmethod
    def PrintMenu():
        if config.LANGUAGE == 'en':
            print('Language:', config.LANGUAGE)
            print('Target search:', config.TargetTitle)
            print('1) Enter start link')
            print('2) Change language')
            print('3) Change target')
            print('0) Exit')
        elif config.LANGUAGE == 'ru':
            print('Язык:', config.LANGUAGE)
            print('Цель для поиска:', config.TargetTitle)
            print('1) Ввести ссылку')
            print('2) Поменять язык')
            print('3) Поменять цель')
            print('0) Выйти')

    @staticmethod
    def ChangeTarget():
        heading = None
        if config.LANGUAGE == 'en':
            heading = config.TitleEN
        elif config.LANGUAGE == 'ru':
            heading = config.TitleRU
        for i in range(len(heading)):
            print(f'{i + 1}) {heading[i]}')
        target_id = int(input())
        config.ChangeTarget(target_id - 1)

    @staticmethod
    def ChangeLanguage():
        print('1) English')
        print('2) Русский')
        tmp = int(input())
        if tmp == 1:
            config.ChangeLanguage('en')
        else:
            config.ChangeLanguage('ru')
