class calcComb():

    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)

    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def setStringa(self):
       self.__stringa = 'casa'
        
       return self.__stringa
    
    def charRipetuti(self):
        '''
        questo metodo deve creare un dictionary all'interno del quale la chiave deve essere
        il singolo carattere, il valore deve essere il numero di ripetizioni di quel carattere
        
        esempi di dictionary sono presenti nel file elementi_base/dictionary.py
        '''
    
    def conta(str):
        word = list("giraffa")  
        carattere = {}
        nCaratteri = 0
        count = 0
        carattereRip = {} 
        for i in word:
         if (i in carattere):  
          carattere[str(i)] += 1
         else:
          carattere[str(i)] = 1 
        for i in carattere:
         print(i)
        if carattere[i] >= 2:  
         carattereRip[i] = carattere[i] 
        print(carattereRip)
        print(carattere)

    def cerca(str):
        str= "pop" 
        it = 'words.italian.txt' 
        f = open(it, 'r')
        line = f.readline()
        for line in f: 
         if str == line[:-1]: 
          print("vero")
        pass

    def fattoriale(n,self):
        stringa = 'gatto'
        n = len(stringa)
        nuova_n = n-1
        while nuova_n>=2:
          permut = n*n-1
          nuova_n = nuova_n-1
        return permut


    def coeffBinom(n, k):
        ''' 
        implementare la formula del coefficiente binomiale a partire dal fattoriale
        questo metodo può essere evitato se ri richiama una delle funzioni built in
        delle librerie standard
        '''
        pass

    def anagrammi(self):
        from itertools import permutations
        lettere = list("casa")
        permutazioni = list(permutations(lettere))
        temp = ''
        anagrammi = []
        for i in permutazioni:
         for carattere in i:
          temp += carattere 
          anagrammi.append(temp)
          temp = ''
    print(anagrammi)
    pass
    
    def confUtil(self):
        open words.italian.txt
        if self.__stringa in words.italian.txt:
           return self.__stringa

    # PERMUTAZIONI

    def nPermutSenzaRip(self):
        

     def nPermutConRip(self):
        '''
        restituire il numero di permutazioni CON ripetizione
        '''
        return 0

    def permutSenzaRip(self):
        '''
        generare e restituire la lista di permutazioni SENZA ripetizione
        '''
        return 0

    def permutConRip(self):
        '''
        generare e restituire la lista di permutazioni CON ripetizione
        '''
        return 0

    # DISPOSIZIONI

    def nDispSemplSenzaRip(self):
        '''
        restituire il numero di disposizioni semplici SENZA ripetizione
        '''
        return 0

    def nDispSemplConRip(self):
        '''
        restituire il numero di disposizioni semplici CON ripetizione
        '''
        return 0

    def dispSemplSenzaRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici SENZA ripetizione
        '''
        return 0


    def dispSemplConRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici CON ripetizione
        '''
        return 0

    # COMBINAZIONI

    def nCombSemplSenzaRip(self):
        '''
        restituire il numero delle combinazioni SENZA ripetizione
        '''
        return 0

    def nCombSemplConRip(self):
        '''
        restituire il numero delle combinazioni CON ripetizione
        '''
        return 0

    def combSenzaRip(self):
        '''
        generare e restituire la lista delle combinazioni SENZA ripetizione
        '''
        return 0


    def combConRip(self):
        '''
        generare e restituire la lista delle combinazioni CON ripetizione
        '''
        return 0