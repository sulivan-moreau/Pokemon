import pygame
import sys


pygame.mixer.init()

def lancer_intro():
    pygame.init()

    explosion_sound = pygame.mixer.Sound("Code2/pokeball-opening-sound-FX.wav")  # Remplacez "explosion_sound.wav" par le chemin de votre fichier son d'explosion
    pokemon_sound = pygame.mixer.Sound("Code2/Pikachu_-Sound-Effect-_320-kbps_.wav")  # Remplacez "pokemon_sound.wav" par le chemin de votre fichier son de Pokémon


    # Paramètres de la fenêtre
    largeur_fenetre = 800
    hauteur_fenetre = 600
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Introduction Pokémon")

    # Couleurs
    couleur_bleu_ciel = (173, 216, 230)
    couleur_texte = (0, 0, 0)
    couleur_box = (255, 255, 255)
    couleur_contour = (0, 0, 0)

    # Musique de fond
    pygame.mixer.music.load("Code2/intro.mp3")
    pygame.mixer.music.play(-1)  # -1 signifie la répétition indéfinie
    

    # Police pour le texte
    pygame.font.init()
    police = pygame.font.Font(None, 36)

    # Dialogue du personnage
    dialogue = [
        "Bien le bonjour!",
        "Bienvenue dans le monde magique des Pokémon!",
        "Mon nom est Chen! ",
        "Les gens m'appellent souvent le Prof Pokémon!",
        "Pour certains, les Pokémon sont des animaux domestiques. ",
        "Pour d'autres, ils sont un moyen de combattre.",
        "Pour ma part... L'étude des Pokémon est ma profession.",
        "Je suppose que si tu es ici, c'est que tu es aussi intéressé par ces créatures fantastiques. ",
        "Je me réjouis de t'avoir à mes côtés. Je suis sûr que tu vas grandement m'aider!",
        "Ta quête des Pokémon est sur le point de commencer!",
        "Un tout nouveau monde de rêves, d'aventures et de Pokémon t'attend!",
        "Aujourd'hui, tu commenceras ton voyage en choisissant ton premier Pokémon.",
        "Les Pokémon sont des créatures étonnantes avec lesquelles tu feras équipe.",
        "Sélectionne ton Pokémon de départ, affronte ton adversaire et que l'aventure commence!"
    ]

    def afficher_dialogue_progressif(message, x, y, largeur, hauteur):
        surface_texte = pygame.Surface((largeur, hauteur))
        surface_texte.fill(couleur_box)  # Fond de la boîte

        # Boîte de dialogue avec contour noir
        pygame.draw.rect(surface_texte, couleur_contour, (0, 0, largeur, hauteur), 3)
        fenetre.blit(surface_texte, (x, y))
        pygame.display.flip()

        mots = message.split()  # Diviser le message en mots
        texte = ""
        lignes = []

        for mot in mots:
            texte_surface = police.render(texte + mot, True, couleur_texte)
            # Si la largeur du texte dépasse la largeur de la boîte, ajouter la ligne à la liste
            if texte_surface.get_width() > largeur - 20:  # 20 est une marge
                lignes.append(texte)
                texte = mot + " "
            else:
                texte += mot + " "

        # Ajouter la dernière ligne si elle n'est pas vide
        if texte:
            lignes.append(texte)

        # Afficher les lignes progressivement
        for i, ligne in enumerate(lignes):
            texte_progressif = ""
            for j, lettre in enumerate(ligne):
                texte_progressif += lettre
                surface_texte.fill(couleur_box)  # Effacer le texte précédent
                pygame.draw.rect(surface_texte, couleur_contour, (0, 0, largeur, hauteur), 3)
                surface_texte.blit(police.render(texte_progressif, True, couleur_texte), (10, 10))
                fenetre.blit(surface_texte, (x, y))
                pygame.display.flip()
                pygame.time.wait(50)  # Pause de 50 millisecondes entre chaque lettre

        # Attendre l'appui sur espace ou clic gauche après avoir écrit toutes les lignes
        attente = True
        while attente:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                    attente = False

        # Effacer le texte en remplissant la surface avec la couleur de fond de la boîte
        surface_texte.fill(couleur_box)
        fenetre.blit(surface_texte, (x, y))
        pygame.display.flip()
        pygame.time.wait(500)  # Pause de 500 millisecondes avant d'afficher la phrase suivante

    def explosion_et_pokemon():

        explosion_image = pygame.image.load("Code2/explode-flash-cartoon-explosion-star-burst-explode-flash-cartoon-explosion-star-burst-isolated-white-background-103618832.jpg.webp")
        explosion_image = pygame.transform.scale(explosion_image, (125, 160))
        explosion_rect = explosion_image.get_rect(topleft=(200, 300))

        deuxieme_image = pygame.image.load("Code2/pik.jpeg")
        deuxieme_image = pygame.transform.scale(deuxieme_image, (100, 120))
        deuxieme_rect = deuxieme_image.get_rect(topleft=(220, 320))

        # Chronomètre pour le temps d'affichage de l'explosion
        start_time = pygame.time.get_ticks()
        duration_explosion = 1500  # Durée en millisecondes

        explosion_sound.play()

        # Chronomètre pour le temps d'affichage de l'explosion
        start_time = pygame.time.get_ticks()
        duration_explosion = 1500  # Durée en millisecondes

        while pygame.time.get_ticks() - start_time < duration_explosion:
            fenetre.blit(explosion_image, explosion_rect.topleft)
            pygame.display.flip()

        explosion_sound.stop()

        # Chronomètre pour le temps d'affichage du Pokémon
        start_time_pokemon = pygame.time.get_ticks()
        duration_pokemon = 2000  # Durée en millisecondes

        pokemon_sound.play()

        while pygame.time.get_ticks() - start_time_pokemon < duration_pokemon:
            fenetre.blit(deuxieme_image, deuxieme_rect.topleft)
            pygame.display.flip()

        pokemon_sound.stop()

        pygame.time.wait(1000)  # Pause de 1000 millisecondes avant de passer à la suite



    # Affichage progressif de l'interface
    def afficher_interface_progressive():
        fond_noir = pygame.Surface((largeur_fenetre, hauteur_fenetre))
        fond_noir.fill((0, 0, 0))
        fenetre.blit(fond_noir, (0, 0))
        pygame.display.flip()

        # Animation "fondu" pour l'arrière-plan
        for i in range(0, 255, 5):
            pygame.time.Clock().tick(60)
            fenetre.fill((i, i, 255))  # Transition vers le bleu ciel
            pygame.display.flip()

        # Chargement de l'image du personnage
        personnage_image = pygame.image.load("Code2/Chen1.png")
        personnage_rect = personnage_image.get_rect(center=(largeur_fenetre // 2.1, hauteur_fenetre // 2.3))

        # Animation "fondu" pour l'apparition de l'image
        for i in range(255):
            pygame.time.Clock().tick(60)
            fenetre.blit(fond_noir, (0, 0))
            personnage_surface = pygame.Surface((700, 500), pygame.SRCALPHA)
            personnage_surface.fill((255, 255, 255, i))
            fenetre.blit(personnage_surface, (50, 50))
            fenetre.blit(personnage_image, personnage_rect.topleft)

            # Ajout de l'explosion après la 6e phrase
            if index_dialogue == 5:
                explosion_et_pokemon()

            pygame.display.flip()

        pygame.time.wait(500)  # Pause de 500 millisecondes avant d'afficher la phrase suivante

    # Boucle principale
    clock = pygame.time.Clock()
    running = True
    index_dialogue = 0

    # Animation initiale de l'interface
    afficher_interface_progressive()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Affichage progressif du dialogue
        if index_dialogue < len(dialogue):
            afficher_dialogue_progressif(dialogue[index_dialogue], 100, hauteur_fenetre - 150, largeur_fenetre - 200, 100)
            index_dialogue += 1

            # Vérifiez si c'est la 6ème phrase pour déclencher l'explosion et l'apparition du Pokémon
            if index_dialogue == 6:
                explosion_et_pokemon()

        # Si tous les dialogues ont été affichés, arrêtez la boucle
        if index_dialogue >= len(dialogue):
            running = False

        pygame.display.flip()
        clock.tick(30)  # Limite de 30 images par seconde

    pygame.mixer.music.stop()

lancer_intro()