import requests


def getAllProduct():
    return requests.get("http://monserveur/product/getProducts")


def getdProductDetails(name):
    return requests.get(f'http://monserveur/product/details/{name}')


def addProduct(product):
    return requests.post("http://monserveur/product/add", json=product)


def deleteProduct(name):
    return requests.delete(f'http://monserveur/product/delete/{name}')


def main():
    isFinished = False
    while(not isFinished):
        print("1 - Afficher tout les produits\n")
        print("2 - Details d'un produit en particulier\n")
        print("3 - Ajouter un produit\n")
        print("4 - Supprimer un produit\n")
        print("5 - Quitter le programme\n")
        choixCourant = input("Veuillez choisir une action : \n")
        choixCourant = int(choixCourant)
        while(choixCourant not in [1, 2, 3, 4, 5]):
            choixCourant = input(
                "Choix incorrect, Veuillez en saisir un nouveau : \n")
            choixCourant = int(choixCourant)
        choix = choixCourant
        if(choix == 1):
            response = getAllProduct()
            print(response.content)
        elif(choix == 2):
            name = input("Saisissez le nom du produit : ")
            response = getdProductDetails(name)
            print(response.content)
        elif(choix == 3):
            idp = input("id nouveau produit : ")
            name = input("Nom du nouveau produit : ")
            price = input("Prix du nouveau produit : ")
            product = {'id': idp, 'name': name, 'price': price}
            response = addProduct(product)
            print(response.content)
        elif(choix == 4):
            name = input("Nom du produit a supprimer : ")
            response = deleteProduct(name)
            print(response.content)
        else:
            print("fini")
            isFinished = True


if __name__ == '__main__':
    main()
