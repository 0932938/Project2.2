import psycopg2, pygame, basic

display = False
class highscores:
    """Deze functie roepen we aan wanneer we op de highscores klikken in het menu
    De parameters zorgen er ook voor dat ik uiteindelijk kan laten zien op het scherm (de kleuren, fonts en x + y"""
    def __init__(self, naam, score, x, y, color):
        self.Naam = naam
        self.Score = score
        self.x = x; self.y = y
        self.Color = color
        self.font = basic.antwoordvak_font

    def highscores_clearen():
        #connect naar database. dbname, user en password. Password = pgadmin4 wachtwoord die je zelf hebt op je postgres
        conn = psycopg2.connect(dbname = 'testdatabase', user='postgres', password='83a7fc0d')

        # met deze lijn kan ik beginnen met normale SQL command in te voeren op python
        cur = conn.cursor()

        cur.execute("DROP TABLE IF EXISTS ranglijst;")
        cur.execute("CREATE TABLE ranglijst (naam varchar, score integer);")

        cur.execute("INSERT INTO ranglijst VALUES (%s, %s)", ('testscore', 50))

        #zorgen dat de data onthouden blijft
        conn.commit()

        cur.execute("SELECT * FROM ranglijst;")

        #data ophalen
        cur.fetchall()

        # Zorgen dat hij niet constant blijft runnen
        cur.close()
        conn.close()

    def highscores_updaten(self):
        conn = psycopg2.connect(dbname='testdatabase', user='postgres', password='83a7fc0d')
        cur = conn.cursor()

        cur.execute("INSERT INTO ranglijst VALUES (%s, %s)", (self.Naam, self.Score))

        conn.commit()
        cur.close()
        conn.close()

    def highscores_display(self, scherm):
        conn = psycopg2.connect(dbname='testdatabase', user='postgres', password='83a7fc0d')
        cur = conn.cursor()

        cur.execute("SELECT * FROM ranglijst ORDER BY score;")
        global display
        while display == False:
            for n in range(0, 10):
                n = n + 1
                score = cur.fetchone()

                highscore = self.font.render(str(score), 0, self.Color)
                basic.screen.blit(highscore, (self.x, self.y))
                self.y += 40
                if n == 10:
                    display = True
                pygame.display.flip()
        conn.commit()
        cur.close()
        conn.close()

naam1 = "Jay"
naam2 = "Kimyiu"
naam3 = "Owen"

beurten1 = 20
beurten2 = 22

# score = highscores(naam3, , None, None,None)
#
# highscores.highscores_updaten(score)

#highscores.highscores_clearen()