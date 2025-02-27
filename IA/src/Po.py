class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            print(f"{montant}€ déposés")
        else:
            print("Le montant du dépôt doit être positif.")

    def retirer(self, montant):
        if 0 < montant <= self.solde:
            self.solde -= montant
            print(f"{montant}€ retirés.")
        elif montant > self.solde:
            print("Fonds insuffisants.")
        else:
            print("Le montant du retrait doit être positif.")

    def afficher_solde(self):
        print(f"Titulaire : {self.titulaire}, Solde actuel : {self.solde}€")


compte = CompteBancaire("Alice", 0)
compte.afficher_solde()
compte.deposer(1000)
compte.afficher_solde()
compte.retirer(2000)
compte.afficher_solde()