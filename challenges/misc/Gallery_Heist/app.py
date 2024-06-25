def get_user_input():
    try:
        user_input = input("Enter the artwork ID you want to view: ")
        return user_input
    except Exception as e:
        print(e)

def view_artwork(artwork_id):
    try:
        print(f"\nfetching artwork: artworks/{artwork_id}.txt ...")
        with open(f"artworks/{artwork_id}.txt", 'r') as file:
            content = file.read()
            print(f"Artwork {artwork_id} description:")
            print(content)
    except FileNotFoundError:
        print("Artwork not found!")

def main():
    print("Welcome to the Virtual Art Gallery Reservation System!")
    print("Explore virtual artworks by entering their IDs.")

    while True:
        print("\nThere are currently only artworks 1.txt, 2.txt, and 3.txt, tut We'll add more in the future!")
        user_input = get_user_input()

        view_artwork(user_input)

if __name__ == "__main__":
    main()
