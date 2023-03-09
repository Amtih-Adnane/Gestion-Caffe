class Coffe():
    def __init__(self,boissans,p_dejonner,la_glace):
        self.boissans = boissans
        self.p_dejonner = p_dejonner
        self.la_glace = la_glace
        # self.prix = prix
    def __str__(self):
        return self.boissans + "," + self.p_dejonner + "," + self.la_glace
    def Menu(self):
        menu = dict()
        glace = ["coupe finte : 30DH", "Coupe Special : 35DH", "Coupe Royal : 35DH", "Coupe enfant : 20DH"]
        menu["Glace "] = str(glace)
        return str(menu)
    def P_dejouner(self):
        Price = 0
        total = 0
        p_dejouner = ["Crock", "Maroccain", "Beldi", "Fassi", "Soussi"]
        prix_p_dejouner = [23,20,20,25,25]
        self.menu_p_dejouner = dict(zip(p_dejouner,prix_p_dejouner))
        print(self.menu_p_dejouner)
        p = "o"
        while p == "o":
            choix = input(("Entre votre petit dejuner")).title()
            if choix in p_dejouner:
                if choix == "Crock":
                    Price = 23
                if choix == "Maroccain":
                    Price = 20
                if choix == "Beldi":
                    Price = 20
                if choix == "Fassi":
                    Price = 25
                if choix == "Beldi":
                    Price = 20
                if choix == "Soussi":
                    Price = 25
            total += Price
            p = input(("Entre o pour continue le choisier ou n pour arreter"))
        return str(total) + " DH"
    def Boissans(self):
        Price = 0
        total = 0
        boissans = ["Caffe au lait", "Caffe Noir", "Tea", "Colacao","Jus d'orange","Jus de citron","Jus de Ananas","Jus d'avocat","Jus Panache"]
        prix_boissans = [10,9,9,13,14,16,16,20,20]
        self.menu_boissans = dict(zip(boissans,prix_boissans))
        print(self.menu_boissans)
        p = "o"
        while p == "o":
            choix = input(("Entre votre Boissans"))
            if choix in boissans:
                if choix == "Caffe au lait ":
                    Price = 10
                if choix == "Caffe Noir":
                    Price = 9
                if choix == "Tea":
                    Price = 9
                if choix == "Colacao ":
                    Price = 25
                if choix == "Jus d'orange ":
                    Price = 14
                if choix == "Jus de citron ":
                    Price = 16
                if choix == "us de Ananas ":
                    Price = 16
                if choix == "Jus d'avocat ":
                    Price = 20
                if choix == "Jus Panache ":
                    Price = 20
            total += Price
            p = input(("Entre o pour continue le choisier ou n pour arreter"))
        return str(total) + " DH"
    def Glace(self):
        Price = 0
        total = 0
        # glace = ["Caffe au lait", "Caffe Noir", "Tea", "Colacao","Jus d'orange","Jus de citron","Jus de Ananas","Jus d'avocat","Jus Panache"]
        glace = ["Coupe finte", "Coupe Special", "Coupe Royal", "Coupe enfant"]
        prix_glace = [30, 35, 35, 20]
        self.menu_glace = dict(zip(glace,prix_glace))
        print(self.menu_glace)
        p = "o"
        while p == "o":
            choix = input(("Entre votre Glace"))
            if choix in glace:
                if choix == "Coupe finte":
                    Price = 30
                if choix == "Coupe Special ":
                    Price = 35
                if choix == "Coupe Royal":
                    Price = 35
                if choix == "Coupe enfant":
                    Price = 20
                if choix == "Coupe de la maison":
                    Price = 40
            total += Price
            p = input(("Entre o pour continue le choisier ou n pour arreter"))
        return total
p1 = Coffe("Colacao","Crock","Coupe finte")
print(p1.P_dejouner())
print(p1.Boissans())
print(p1.Glace())