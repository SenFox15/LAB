def swap_words(input_filename, output_filename):
    
    try:
        with open(input_filename, "r") as infile, open(output_filename, "w") as outfile:
            for line in infile:
                words = line.split()
                if words: 
                    shortest_word = min(words, key=len)
                    longest_word = max(words, key=len)
                    words = [shortest_word if word == longest_word else longest_word if word == shortest_word else word for word in words] 
                    outfile.write(" ".join(words) + "\n")
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



swap_words("input.txt", "output.txt")
print("Word swapping complete. Results written to output.txt")