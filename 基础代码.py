import codecs

#读
f = codecs.open("you_file.txt", "r", "utf-8")
line = f.readline()

#写
f = codecs.open("you_file.txt", "w", "utf-8")
txt = unicode("中文1", "utf-8")
f.write(txt)
f.write(u'中文2\n')
f.flush()
f.close()
