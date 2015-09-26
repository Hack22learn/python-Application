__auther__='Sudhanshu Patel'
import xlrd

#find top 3 frequently occuring  genere
Wbook = xlrd.open_workbook('PicturePerfect.xlsx') #global data

def TopGenere(limit=3):
    #top n genere
    #print 'no of sheets ',Wbook.nsheets
    # we r goint to process only first sheet
    data = Wbook.sheet_by_index(0)
    
    genreState=dict()
    for row in range(1,data.nrows):
        gsplit=data.row_values(row)[1].split(',')
        for genre in gsplit:
            if genre in genreState:
                genreState[genre]+=1
            else:
                genreState[genre] =1
    #now find top limit no of genere
    ls=genreState.values()
    ls.sort(reverse=True)
    topgenre=[[ls[0]],[[ls[1]]],[ls[2]]]
    print len(topgenre)
    for genre in genreState:
        if genreState[genre]==ls[0]:
            topgenre[0].append(genre)
        elif genreState[genre]==ls[1]:
            topgenre[1].append(genre)
        elif genreState[genre]==ls[2]:
            topgenre[2].append(genre)

    #print "top 3 count genre'
    print topgenre[0]
    print topgenre[1]
    print topgenre[2]
if __name__=='__main__':
    TopGenere()


