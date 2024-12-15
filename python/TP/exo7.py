def Sanction_Vitesse(ExesVit, limite): 
    amende = 0
    nb_Pts = 12
    Susp_Permis = 0
    if ExesVit > 20 and limite >= 50 :
        if ExesVit <= 30 : 
            amende = 45
            nb_Pts -=1
            Susp_Permis = 0
            #print(amende,nb_Pts,Susp_Permis)

        elif ExesVit > 20 and limite < 50 :
            if ExesVit <= 30 :
                amende = 90
                nb_Pts = 1
                Susp_Permis = 0
                #print(amende,nb_Pts,Susp_Permis)

        elif ExesVit > 20 and ExesVit < 30 :
            amende = 90
            nb_Pts -=2
            Susp_Permis = 0
            #print(amende,nb_Pts,Susp_Permis)

        elif ExesVit > 30 and ExesVit < 40 :
            amende = 90
            nb_Pts -=3
            Susp_Permis = 3
            #print(amende,nb_Pts,Susp_Permis)
    
        elif ExesVit > 40 and ExesVit < 50 :
            amende = 90
            nb_Pts -=4
            Susp_Permis = 3
            #print(amende,nb_Pts,Susp_Permis)

        elif ExesVit > 50 :
            amende = 1500
            nb_Pts -=6
            Susp_Permis = 3
            #print(amende,nb_Pts,Susp_Permis)

        else : 
            print("Vous êtes en règles :)")
    
    return amende, nb_Pts, Susp_Permis 
    
print(Sanction_Vitesse(60,50))

    
