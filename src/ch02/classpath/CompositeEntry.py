from ch02.classpath.Entry import Entry

class CompositeEntry(Entry):
    def __init__(self):
        self.compositeEntryList = []

    def newCompositeEntry(pathList):
        compositeEntry = CompositeEntry()
        for _, path in pathList.split(Entry.pathListSeparator):
            entry = Entry.newEntry(path)
            compositeEntry.compositeEntryList.append(entry)
        return compositeEntry

    def readClass(self,className):
        for entry in self.compositeEntryList:
            data, fromEntry, error = entry.readClass(className)
            if not error:
                return data, fromEntry, None
        return None, None, "class not found:{0}".format(className)

    def __str__(self):
        return Entry.pathListSeparator.join(str(entry) for entry in self.compositeEntryList)