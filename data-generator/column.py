class Column:
    # Les colonnes
    def longueur_total(self,language):
        total_length = sum(len(word) for word in language)
        return total_length

    def nombre_de_mot(self,language):
        num_words = len(language)
        return num_words

    def longueur_maximal(self,language):
        max_length = max(len(word) for word in language)
        return max_length

    def calculate_zero_ratio(self,language):
        total_characters = ''.join(language)
        num_zeros = sum(1 for char in total_characters if char == "0")
        zero_ratio = num_zeros / len(total_characters) if len(total_characters) > 0 else 0
        return zero_ratio

    def calculate_one_ratio(self,language):
        total_characters = ''.join(language)
        num_ones = sum(1 for char in total_characters if char == "1")
        one_ratio = num_ones / len(total_characters) if len(total_characters) > 0 else 0
        return one_ratio

    def calculate_bit_changes(self,language):
        num_changes = sum(1 for i in range(1, len(language)) if language[i] != language[i-1])
        return num_changes

    # existance de prefixe
    def is_prefix_code(self,langage):
        langage = sorted(langage, key=len)
        n = len(langage)
        
        for i in range(n):
            for j in range(i+1, n):
                if langage[j].startswith(langage[i]):
                    return 0 
        
        return 1

    # nombre de prefixe
    def calculate_prefix_count(self,language):
        prefixes = set()
        count = 0
        for word in language:
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix not in prefixes:
                    prefixes.add(prefix)
                    count += 1
        return count