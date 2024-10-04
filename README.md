# STEPS:
- Allez sur : *https://googlechromelabs.github.io/chrome-for-testing/*  
et telechargez *the stable version* pour votre appareil
- Allez dans chrome, puis 3 petits points, puis parametres. Descendez en bas fla barre a gauche et allez sur *A propos de chrome*. Lanzez la mise a jour (et relancez le navigateur si demandé).
- C quasi fini ! Allez sur *const.py* et changez :
    - PROFILE_PATH : Bedlo berk *C:\\Users\\Ryolin* par le path ta3 votre profil. Gardez la suite.
    - PATH : Le chemin de l'executable du dossier telechargé précédemment (chromedriver.exe).
- Creez un environnement, par exemple via ces commandes:
    - pip install pipenv (si vous ne l'avez pas deja)
    - pipenv shell
- Telechargez les dependancies : **pip install -r requirements.txt**
- C bon ! Lancez le script avec : **python scrape.py**