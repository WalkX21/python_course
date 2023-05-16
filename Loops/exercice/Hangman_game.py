import random # le import nous permet d'importer les fonction de la library Random

words = ['father', 'entreprise', 'science'] # On crée une variable words et on met dedans une liste contenant des chaines de caractères

word = random.choice(words) #on crée une variable ou on met un mot aléatoire de la liste words en utilisant choice

guesses = ''  # on crée une variable str vide, qui permet de stoker les lettres qu'on a pu deviner 
turns =  10   # on crée une variable qui definit le nombre de test possible

while turns > 0: # while est une boucle qui prend comme condition que turns doit superieur à 0
    print(f"You have {turns} turns left") #turns definit le nombre d'essai restant, ce print dit combien de tours il reste;

    guessed_all = True #
    for c in word :  # c ==> characters, word est une chaines de caractère , la boucle permet de prendre une caractère de la chaines
        if c in guesses:  #si c est dans guessesn le resultat est booleen donc soit  vrai ou faux
            print(c)
        else:
            print('_', end=' ',)  #si c n'est dans le mot aleatoires n'est pas dans guesses, on le remplace par _ separés par des espaces
            guesses_all = False
    print()

    if not guessed_all:  #si on a pas deviné tous les characters 
        guess = input ("Guess à characters!") #on crée une variable guess, ou sera stocker les propositions du joueur.
        guesses = guesses + guess  #on implemente dans la variable definit plus haut le characteres proposés par le joueur
        if guess not in word: #si sa proposition n'est pas dans la mot aléatoire 
            turns = turns - 1 #on enleve un tour
    else:
        turns = 0 #sinon plus de tours, la partie est fini


