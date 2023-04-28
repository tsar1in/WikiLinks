from queue import Queue
import src.parser_wiki as parser
import src.config as config


class Logic:
    def __init__(self):
        self.result_path = dict()
        self.wrong_links_queue = Queue()

    def SearchPath(self):
        if config.LANGUAGE == 'en':
            print("Enter link: ", end='')
        elif config.LANGUAGE == 'ru':
            print("Введите ссылку: ", end='')
        start_link = str(input())
        path = self.FindPath(start_link)
        print(' --> '.join(path), '\n')
        if config.LANGUAGE == 'en':
            print("Click <Enter> to return to menu ", end='')
        elif config.LANGUAGE == 'ru':
            print("Нажмите <Enter>, чтобы вернуться в меню ", end='')
        input()

    def FindPath(self, start_url):
        if start_url == config.TargetLink:
            return [config.TargetTitle]
        self.__init__()
        self.result_path[start_url] = []
        self.wrong_links_queue.put(start_url)
        while not self.wrong_links_queue.empty():
            if self.BFSlinks(self.wrong_links_queue.get()):
                break
        return self.result_path[config.TargetLink] + [config.TargetTitle]

    def BFSlinks(self, cur_link):
        path = self.result_path[cur_link]
        try:
            wiki_title, all_links = parser.FindLinksFromWiki(cur_link)
        except Exception:
            return False
        if config.TargetLink in all_links:
            self.result_path[config.TargetLink] = path + [wiki_title]
            return True
        for i in (all_links & config.TargetHints):
            if (i in self.result_path) and (len(self.result_path[i]) <= len(path)):
                continue
            self.result_path[i] = path + [wiki_title]
            if self.BFSlinks(i):
                return True
        for i in all_links:
            if (i in self.result_path) and (len(self.result_path[i]) <= len(path)):
                continue
            self.result_path[i] = path + [wiki_title]
            self.wrong_links_queue.put(i)
