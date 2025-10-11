
def python_interview():
    print('Iniciando')

# 🎯 CORE: Lists & Dicts (65% do foco)
# Estas são as estruturas mais cobradas em entrevistas técnicas.

    # Exercício 1: Anagramas Agrupados ⭐⭐⭐
    # Dada uma lista de strings, agrupe todos os anagramas juntos.

    # Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
    # Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = dict()
    for word in input:
        l = sorted(word)
        res_key = tuple(l)
        if res_key not in res:
            res[res_key] = []
        res[res_key].append(word)
    l = list(res.values())
    print(type(l))
    print(type(res))

    print(l)

# Exercício 2: Top K Elementos Frequentes ⭐⭐⭐
# Encontre os k elementos mais frequentes em uma lista.

    # pythonInput: nums = [1,1,1,2,2,3], k = 2
    # Output: [1, 2]
    # Conceitos: Counter (dict), heap ou bucket sort com list

    nums = [2,2,1,1,1,3]
    k=2
    
    my_set = set(nums)
    res = dict()
    for i in my_set:
        res.setdefault(i,nums.count(i))
    
    print(res)
    sorted_res = sorted(res.items(),key=lambda x: x[1], reverse=True)
    print(sorted_res)

    top_k = [key for key, value in sorted_res[:k]]
    print(top_k)
    



if __name__ == "__main__":
    python_interview()
