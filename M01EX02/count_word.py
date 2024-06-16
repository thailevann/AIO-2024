#!gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
def count_word(file_path):
    counter = {}
    file_object = open(file_path)
    file_object_lines = file_object.readlines()
    end_word = [".", ","]
    for line in file_object_lines:
        word_list = line.split(" ")
        for w in word_list:
            w = w.lower().strip().replace(",", "").replace(".", "").replace("\n", "")

            if w in counter:
                counter[w] += 1
            else:
                counter[w] = 1
    return counter


file_path = "./content/P1_data.txt"
result = count_word(file_path)
print(result['man'])
assert result['who'] == 3
