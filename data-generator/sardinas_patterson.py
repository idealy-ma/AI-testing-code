class Sardinas_Patterson:
    # Sardinas and patterson
    def multiply(self,lang1, lang2):
        newLang = set()
        for u in lang1 :
            for v in lang2 :
                if len(u) >= len(v) and u.find(v) == 0:
                    newLang.add(u[len(v):])
        return newLang

    def removeVoid(self,language):
        result = set()
        for u in language:
            if u != '' :
                result.add(u)

        return result

    def sardinas_patterson(self,language):
        uN = self.removeVoid(self.multiply(language, language))
        uN_1 = []
        while True :
            uN_1.append(set(uN))
            uN = self.multiply(uN, language).union(self.multiply(language, uN))
            
            for value in uN :
                if value == "":
                    return 0

            for value in uN_1 :
                if value == uN :
                    return 1
