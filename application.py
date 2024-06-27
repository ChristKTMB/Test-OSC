import requests

def create_article():
    data = {
        "title": input("Entrez le titre de l'article: "),
        "auteur": input("Entrez le nom de l'auteur: "),
        "content": input("Entrez le contenu de l'article: ")
    }
    response = requests.post(orange_api_url, json=data)
    print("Création reussi:", response.json())

def list_articles():
    response = requests.get(orange_api_url)
    print("Liste des articles:", response.json())

def get_article():
    article_id = input("Entrez l'ID de l'article à récupérer: ")
    response = requests.get(f"{orange_api_url}{article_id}/")
    print("Détails de l'article:", response.json())

def update_article():
    article_id = input("Entrez l'ID de l'article à mettre à jour: ")
    data = {
        "title": input("Entrez le nouveau titre de l'article: ")
    }
    response = requests.put(f"{orange_api_url}{article_id}/", json=data)
    print("Réponse de la mise à jour:", response.json())

def delete_article():
    article_id = input("Entrez l'ID de l'article à supprimer: ")
    response = requests.delete(f"{orange_api_url}{article_id}/")
    print("Code de statut de suppression:", response.status_code)

orange_api_url = "http://127.0.0.1:8000/api/articles/"

def main():
    while True:
        print("\nChoisissez une opération :")
        print("1. Créer un article")
        print("2. Lister tous les articles")
        print("3. Récupérer un article par ID")
        print("4. Mettre à jour un article")
        print("5. Supprimer un article")
        print("6. Quitter")
        
        choice = input("Entrez le numéro de l'opération à effectuer: ")
        
        if choice == "1":
            create_article()
        elif choice == "2":
            list_articles()
        elif choice == "3":
            get_article()
        elif choice == "4":
            update_article()
        elif choice == "5":
            delete_article()
        elif choice == "6":
            print("Sortie du programme.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
