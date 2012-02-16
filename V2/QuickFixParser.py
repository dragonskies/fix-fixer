from collections import OrderedDict

RepeatingTags = ['146', '268', '555']

class QuickFixParser:
    def __init__(self, string=None, file=None):
        if not string:
            file = open(file)
            string = file.read()
        self.tags = string.split('\x01')
        self.tag_pairs = []
        for tag in self.tags:
            self.tag_pairs.append(self.SplitPair(tag))
        self.Dictionary()


    def Dictionary(self):
        self.dictionary = OrderedDict()
        RepeatCount = 0
        RepeatTag = None
        RepeatSubTag = None
        message_num = 1
        for tag in self.tag_pairs:
            try:
                if tag[0] == '10':
                    RepeatCount = 0
                    RepeatTag = None
                    RepeatSubTag = None
                    self.dictionary[tag[0]] = tag[1]
                if tag[0] not in RepeatingTags and RepeatCount == 0:
                    self.dictionary[tag[0]] = tag[1]
                elif tag[0] in RepeatingTags and RepeatCount == 0:
                    RepeatSubTag = 'Message ' + str(message_num)
                    self.dictionary[tag[0]] = (tag[1], OrderedDict())
                    self.dictionary[tag[0]][1][RepeatSubTag] = OrderedDict()
                    RepeatTag = tag[0]
                    RepeatCount = int(tag[1])
                elif RepeatCount > 0:
                    if tag[0] in self.dictionary[RepeatTag][1][RepeatSubTag].keys():
                        message_num += 1
                        RepeatCount -= 1
                        RepeatSubTag = 'Message ' + str(message_num)
                        self.dictionary[RepeatTag][1][RepeatSubTag] = OrderedDict()
                    self.dictionary[RepeatTag][1][RepeatSubTag][tag[0]] = tag[1]
            except IndexError:
                pass
        return self.dictionary
            

    def SplitPair(self, tag):
        return tag.split('=')

    def CombinePair(self, key):
        value = self.dictionary[key]
        return str(key) + "=" + str(value)

    def Spacing(self, length):
        string = ""
        for i in range(length):
            string = string + " "
        return string

if __name__=='__main__':
    QuickFixParser(file='multi_google')
