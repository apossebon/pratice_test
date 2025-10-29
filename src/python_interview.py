
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

# Exercício 3: Subarray com Soma K ⭐⭐⭐
# Encontre o número de subarrays contínuos cuja soma é igual a k.
    # pythonInput: nums = [1,1,1], k = 2
    # Output: 2  # [1,1] aparece 2 vezes
    # Conceitos: Prefix sum com dict para memoização
    nums = [1,1,1]
    k = 2

    prefix_sum = 0
    count = 0
    sum_dict = {0: 1}

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in sum_dict:
            count += sum_dict[prefix_sum - k]
        sum_dict[prefix_sum] = sum_dict.get(prefix_sum, 0) + 1

    print(count)


# Exercício 4: Merge Intervals ⭐⭐
# Mescle intervalos sobrepostos.
    # pythonInput: [[1,3],[2,6],[8,10],[15,18]]
    # Output: [[1,6],[8,10],[15,18]]
    # Conceitos: List de listas, sorting, manipulação de intervalos
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals.sort(key=lambda x: x[0])
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    print(merged)


if __name__ == "__main__":
    python_interview()
