from funcions import login, personatge_aventura

def main():
    if login():
        personatge_aventura()
        print("\n--- Iniciant l'aventura ---")
    else:
        print("\nTorna a intentar-ho.")

if __name__ == "__main__":
    main()