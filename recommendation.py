print("===== Movie Recommendation System =====")

genre = input("Enter genre (action/comedy/romance/horror): ").lower()

if genre == "action":
    print("\nRecommended Movies:")
    print("1. Avengers")
    print("2. John Wick")
    print("3. Mission Impossible")

elif genre == "comedy":
    print("\nRecommended Movies:")
    print("1. 3 Idiots")
    print("2. Dhamaal")
    print("3. Golmaal")

elif genre == "romance":
    print("\nRecommended Movies:")
    print("1. Jab We Met")
    print("2. Veer-Zaara")
    print("3. DDLJ")

elif genre == "horror":
    print("\nRecommended Movies:")
    print("1. The Conjuring")
    print("2. Annabelle")
    print("3. Insidious")

else:
    print("Sorry! Genre not available.")
