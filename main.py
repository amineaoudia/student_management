from grade_manager import GradeManager


def show_menu():
    print("\n===== MENU - Gestion des notes =====")
    print("1. Afficher la moyenne generale")
    print("2. Afficher la mediane")
    print("3. Afficher l'ecart-type")
    print("4. Afficher la meilleure note")
    print("5. Afficher la pire note")
    print("6. Afficher les etudiants admis")
    print("7. Afficher les etudiants ajournes")
    print("0. Quitter")


def main():
    manager = GradeManager("notes.csv")
    manager.load_data()

    while True:
        show_menu()
        choice = input("Votre choix : ")

        if choice == "1":
            print(f"Moyenne generale : {manager.average_grade():.2f}")

        elif choice == "2":
            print(f"Mediane : {manager.median_grade():.2f}")

        elif choice == "3":
            print(f"Ecart-type : {manager.standard_deviation():.2f}")

        elif choice == "4":
            print(f"Meilleure note : {manager.best_student()}")

        elif choice == "5":
            print(f"Pire note : {manager.worst_student()}")

        elif choice == "6":
            admitted = manager.admitted_students()
            print(f"Etudiants admis ({len(admitted)}) :")
            for s in admitted:
                print(f" - {s}")

        elif choice == "7":
            failed = manager.failed_students()
            print(f"Etudiants ajournes ({len(failed)}) :")
            for s in failed:
                print(f" - {s}")

        elif choice == "0":
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Reessayez")


if __name__ == "__main__":
    main()
