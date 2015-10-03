import xlrd,anydbm
#find top 3 frequently occuring  genere
Wbook = xlrd.open_workbook('PicturePerfect.xlsx') #global data

def Rating_Cast():
    #Rating Actor and director
    #we are giving priority to each
    #ie. director get priority of 4
    # acter get priority of 4,3,2,1 according to order
    # !st acter priority 4 , secong get 3
    #third get 3 and remainig got 1
    #then divide rate*number_of_people_rate in given ratio and assign to them
    data = Wbook.sheet_by_index(0)
    #counter=0
    director=dict()
    actor=dict()
    for row in range(1,data.nrows):
        #counter+=1
        #if counter %100==0:
        #   print 'record completed',counter
        flag=True
        for col in [2,3,4,5]:
            if col not in [2,3]:
                ls=data.row_values(row)[col].split(',')
            else:
                ls=data.row_values(row)[col]
            #print ls
            if flag and col == 2:
                rate = float(ls)
                #print '_________rate',rate
            elif flag and col == 3:
                #claculate rating * number of people rate
                rate *=float(ls)
                #print '__________rateC',rate
            elif flag and col == 4: #cast
                cast=ls
                ratio=[4,3,2,1]
                if len(ls)>4 :
                    for i in range(len(ls)-4):
                        ratio.append(1)
                    #print '__________cast',cast
                    #print '__________ratio',ratio
            elif flag and col==5:
                directr=ls
        # start calculating contribution
        if flag:
            sum_r=sum(ratio)+4 #+4 for direcor priority
            per_unit=rate/sum_r
            if directr[0] not in director:
                director[directr[0]]=[1,(4*per_unit)] #index 0 elemet shows number of movies he make
            else:
                director[directr[0]].append(4*per_unit)
                director[directr[0]][0]+=1
            for i in range(len(cast)):
                if cast[i] not in actor:
                    actor[cast[i]]=[1,ratio[i]*per_unit]  #index 0 shows number of movies he have done
                else:
                    actor[cast[i]].append(ratio[i]*per_unit)
                    actor[cast[i]][0]+=1
    return(actor,director)

def average_Rating(actor,director):
    #calculate average
    for actr in actor:
        sum_r=sum(actor[actr][1:])
        l=len(actor[actr][1:])
        actor[actr]=(sum_r/l)*(actor[actr][0]/float(500))
    for directr in director:
        sum_r=sum(director[directr][1:])
        l=len(director[directr][1:])
        director[directr]=(sum_r/l)*(director[directr][0]/float(500))

    return (actor,director)

def file_write(actor,director):
    f=open("Actor.data",'w')
    for act in actor:
        f.write(act+", "+str(actor[act])+ '\n')
    f.close()
    f=open('director.data','w')
    for dt in director:
        f.write(dt+", "+str(director[dt])+'\n')
    f.close()

'''def database(actor,director):
    db_a = anydbm.open('actor.anydb', 'c')
    for key in actor:
        db_a[key]=actor[key][1]
    db_a.close()
    db_d=anydbm.open('director.anydb', 'c')
    for key in director:
        db_d[key]=director[key][1]
    db_d.close()

'''
def Rating_movies(actor,director):
    #rate Movies = rating*number of people rate +rating of each cast and actor
    data = Wbook.sheet_by_index(0)
    movies=dict()
    for row in range(1,data.nrows):
         for col in [0,2,3,4,5]:
            if col==0:
                mov=data.row_values(row)[col]
                movies[mov]=1
                #print '.......Movie',mov
            elif col==2:
                movies[mov]=float(data.row_values(row)[col])
                #print '.......rate',movies[mov]
            elif col ==3:
                movies[mov] *=float(data.row_values(row)[col])
                #print '.......Nrate',movies[mov]
            elif col==4:
                ls=data.row_values(row)[col].split(',')
                #print '.......actor',ls
                for key in ls:
                    movies[mov] +=actor[key]
            elif col==5:
               # print '.......directorB',movies[mov]
                movies[mov] += director[data.row_values(row)[col]]
               # print '.......directorF',movies[mov]
    return movies

def Top_10(movies):
    #return top 10 movies of all time
    rate=movies.values()
    rate.sort(reverse=True)
    #print rate[1:5]
    #print rate[560:565]
    #print rate[-5:]
    
    mov=[False,False,False,False,False,False,False,False,False,False]
    for key in movies:
        if movies[key]==rate[0]:
            mov[0]=key
        elif movies[key]==rate[1]:
            mov[1]=key
        elif movies[key]==rate[2]:
            mov[2]=key
        elif movies[key]==rate[3]:
            mov[3]=key
        elif movies[key]==rate[4]:
            mov[4]=key
        elif movies[key]==rate[5]:
            mov[5]=key
        elif movies[key]==rate[6]:
            mov[6]=key
        elif movies[key]==rate[7]:
            mov[7]=key
        elif movies[key]==rate[8]:
            mov[8]=key
        elif movies[key]==rate[9]:
            mov[9]=key
        elif False not in mov:
            return mov





        
if __name__=='__main__':
    #top_genre=[u'Drama',u'Comedy',u'Thriller']
    print'**************************************************************************' 
    #genre=top_genre[0]#finding best cast in genre 0 for Drama , 1 for comedy and 2 for Th 
    ratings=Rating_Cast() 
    ratings=average_Rating(ratings[0],ratings[1])
    #NoW find top 10 movies of all time
    movies_R = Rating_movies(ratings[0],ratings[1])
    topMovies=Top_10(movies_R)
    print 'Best Movies of all time'
    for i in range(10):
        print topMovies[i]
    
    
    print "thank you"

