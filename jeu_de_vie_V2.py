########################
# Auteurs:
# Nabil Hamoudi
# Groupe de TD:
# DLBI1
########################

########################
# import des librairies
import tkinter as tk


########################
# Constantes

COULEUR_FOND = "black"
COULEUR_VIE = "yellow"
BORDURE = "white"
LARGEUR = 1000
HAUTEUR = 800
NOMBRE_CASE_R = 8
NOMBRE_CASE_C = 8
RAPORT_CASE_R = HAUTEUR / NOMBRE_CASE_R
RAPORT_CASE_C = LARGEUR / NOMBRE_CASE_C
FIND_LIFE = []
CASE = [[-1 for i in range(NOMBRE_CASE_R)]for u in range(NOMBRE_CASE_C)]
FRAME = 2
TEMP = "1"

life_temp = []
dies_temp = []
FRAMEtemp = FRAME

########################
# fonctions


def quadrillage():
    """Affiche un quadrillage sur le canvas."""
    global RAPORT_CASE_C, RAPORT_CASE_R

    for c in range(NOMBRE_CASE_C):
        taille_c = RAPORT_CASE_C * c
        canvas.create_line(taille_c, 0, taille_c, HAUTEUR, fill=BORDURE)

        for r in range(NOMBRE_CASE_R):
            taille_r = RAPORT_CASE_R * r
            canvas.create_line(0, taille_r, LARGEUR, taille_r, fill=BORDURE)


def Donne_vie(event):
    """Donne vie a une case en fonction du clic"""
    global RAPORT_CASE_C, RAPORT_CASE_R, FIND_LIFE, CASE
    c = int(event.x // RAPORT_CASE_C)
    r = int(event.y // RAPORT_CASE_R)
    if CASE[c][r] != -1:
        canvas.delete(CASE[c][r])
        CASE[c][r] = -1
        FIND_LIFE.remove([c, r])
    else:
        CASE[c][r] = canvas.create_rectangle(
            c * RAPORT_CASE_C, r * RAPORT_CASE_R,
            (c + 1) * RAPORT_CASE_C, (r + 1) * RAPORT_CASE_R,
            outline=BORDURE, fill=COULEUR_VIE)
        FIND_LIFE.append([c, r])


def startgame():
    """commence le jeu de la vie"""
    global RAPORT_CASE_C, RAPORT_CASE_R, FIND_LIFE, life_temp, dies_temp, FRAME, FRAMEtemp, TEMP
    if FIND_LIFE == []:
        pass
    else:
        for f in range(FRAME):
            life_temp = []
            dies_temp = []
            for i in FIND_LIFE:
                comptage(i[0], i[1])
            for i in life_temp:
                if i not in FIND_LIFE:
                    FIND_LIFE.append(i)
            for i in dies_temp:
                if i in FIND_LIFE:
                    FIND_LIFE.remove(i)
            canvas.delete('all')
            affichage(FIND_LIFE)
        if FRAMEtemp != 1:
            canvas.after(TEMP, startgame)
            FRAMEtemp -= 1
        else:
            FRAMEtemp = FRAME


def comptage(c, r):
    """compte l'indice de vie"""
    global FIND_LIFE, life_temp, dies_temp, NOMBRE_CASE_C, NOMBRE_CASE_R, CASE
    R_max = NOMBRE_CASE_R - 1
    C_max = NOMBRE_CASE_C - 1
    for i in range(9):
        C = c - 1 + (i // 3)
        R = r - 1 + (i % 3)
        if [C, R] not in life_temp and [C, R] not in dies_temp and C >= 0 and C <= C_max and R <= R_max and R >= 0:
            COUNT = 0
            for o in [x for x in range(9) if x != 4]:
                C_temp = C - 1 + (o // 3)
                R_temp = R - 1 + (o % 3)
                if C_temp >= 0 and C_temp <= C_max and R_temp <= R_max and R_temp >= 0:
                    if [C_temp, R_temp] in FIND_LIFE:
                        COUNT += 1
            if COUNT <= 1 or COUNT > 3:
                dies_temp.append([C, R])
            elif COUNT == 2:
                if [C, R] not in FIND_LIFE:
                    dies_temp.append([C, R])
            else:
                life_temp.append([C, R])


def affichage(FIND_LIFE):
    """fini la frame du jeu"""
    global CASE, NOMBRE_CASE_R, NOMBRE_CASE_C, RAPORT_CASE_C, RAPORT_CASE_R
    CASE = [[-1 for i in range(NOMBRE_CASE_R)]for u in range(NOMBRE_CASE_C)]
    quadrillage()
    for i in FIND_LIFE:
        C, R = i[0], i[1]
        CASE[C][R] = canvas.create_rectangle(
            C * RAPORT_CASE_C, R * RAPORT_CASE_R,
            (C + 1) * RAPORT_CASE_C, (R + 1) * RAPORT_CASE_R,
            outline=BORDURE, fill=COULEUR_VIE)


########################
# programme principal
racine = tk.Tk()
racine.title("Jeu de la vie")
# création des widgets
canvas = tk.Canvas(racine, bg=COULEUR_FOND, width=LARGEUR, height=HAUTEUR)
Start = tk.Button(
    racine, text="START", font=("helvetica", "20"), command=startgame)
quadrillage()
canvas.bind("<Button-1>", Donne_vie)
# placement des widgets
canvas.grid(row=1, columnspan=3)
Start.grid(row=0, column=1)
# boucle principale
racine.mainloop()
