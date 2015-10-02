import xlrd
#find top 3 frequently occuring  genere
Wbook = xlrd.open_workbook('PicturePerfect.xlsx') #global data

def Rating_Cast(genre):
    #Rating Actor and director
    #we are giving priority to each
    #ie. director get priority of 4
    # acter get priority of 4,3,2,1 according to order
    # !st acter priority 4 , secong get 3
    #third get 3 and remainig got 1
    #then divide rate*number_of_people_rate in given ratio and assign to them
    data = Wbook.sheet_by_index(0)
    
    director=dict()
    actor=dict()
    for row in range(1,4):#data.nrows):
        flag=False
        for col in [1,2,3,4,5]:
            if col not in [2,3]:
                ls=data.row_values(row)[col].split(',')
            else:
                ls=data.row_values(row)[col]
            #print ls
            if col == 1:
                for gnr in genre:
                    if gnr in ls:
                        flag=True
                        break
                #print '_________________',flag
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
		actor[actr]=[actor[actr][0],(sum_r/l)*(actor[actr][0]/float(500))]
	for directr in director:
		sum_r=sum(director[directr][1:])
		l=len(director[directr][1:])
		director[directr]=[director[directr][0],(sum_r/l)*(director[directr][0]/float(500))]

	return (actor,director)

def file_write(actor,director):
	f=open("Actor.data",'w')
	for act in actor:
		f.write(act+", "+", ".join([str(x) for x in actor[act]])+ '\n')
	f.close()
	f=open('director.data','w')
	for dt in director:
		f.write(dt+", "+", ".join([str(x) for x in director[dt]])+'\n')
	f.close()



        
if __name__=='__main__':
    top_genre=[u'Drama',u'Comedy',u'Thriller']
    ratings=Rating_Cast(top_genre)
    ratings=average_Rating(ratings[0],ratings[1])
    file_write(ratings[0],ratings[1])

    print "thank you"

