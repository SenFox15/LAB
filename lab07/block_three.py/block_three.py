import os
import shutil

def find_files(search_term, directory="."):
    
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            if search_term.lower() in file.lower():
                results.append(os.path.join(root, file))
    return results

def rename_item(path, new_name):
   
    try:
        new_path = os.path.join(os.path.dirname(path), new_name)
        os.rename(path, new_path)
        print(f"Renamed '{path}' to '{new_path}'")
    except FileNotFoundError:
        print(f"Error: File or directory '{path}' not found.")
    except OSError as e:
        print(f"Error renaming: {e}")

def move_item(path, dest_path):
    
    try:
        shutil.move(path, dest_path)
        print(f"Moved '{path}' to '{dest_path}'")
    except FileNotFoundError:
        print(f"Error: File or directory '{path}' not found.")
    except OSError as e:
        print(f"Error moving: {e}")
    except shutil.Error as e:
        print(f"Error moving (shutil error): {e}")



def main():
   
    while True:
        print("\nFile Manager Menu:")
        print("1. Find file(s)")
        print("2. Rename file/folder")
        print("3. Move file/folder")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            search_term = input("Enter search term (filename or part of it): ")
            directory = input("Enter directory to search in (default is current): ") or "."  
            found_files = find_files(search_term, directory)
            if found_files:
                print("\nFound files:")
                for file in found_files:
                    print(file)
            else:
                print("No files found matching the search term.")

        elif choice == '2':
            path = input("Enter full path to file/folder: ")
            new_name = input("Enter new name: ")
            rename_item(path, new_name)

        elif choice == '3':
            path = input("Enter full path to file/folder: ")
            dest_path = input("Enter destination path: ")
            move_item(path, dest_path)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
