import bs4, re
for AzovNum in range(31):
    exampleFile = open(r'C:\file.txt_w%s.txt' % (AzovNum + 1), encoding='utf-8') #txt file with html code of pages with news items
    exampleFile1 = exampleFile.read()
    Ze = re.sub(r'</html>', ' ', exampleFile1, flags=re.DOTALL) #removes </html> tag
    headlines = re.compile(r'.title.(.*)\s|\sУкраинская правда..title.') #finds headlines with regular expressions
    head = headlines.findall(exampleFile1)
    headli = '\n'.join(head)
    po = re.compile(r'Порошенко') #finds a surname or a keyword
    por = po.findall(headli)
    pro = len(por) #counts the number of mentions per day
    print(pro)
