def check_anagram(str1, str2):
    list1, list2 = [], []
    for i in str1:
        list1.append(i)

    for j in str2:
        list2.append(j)

    if len(list1) == len(list2):
        list1.sort()
        list2.sort()
    if list1 == list2:
        return True

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash_table = {}
        for i in strs:
            if sum([ord(j) for j in i]) in hash_table:
                flag = False
                for k in hash_table[sum([ord(j) for j in i])]:
                    if check_anagram(i, k[0]):
                        flag = True
                        k.append(i)

                if not flag:
                    hash_table[sum([ord(j) for j in i])].append([i])

            else:
                hash_table[sum([ord(j) for j in i])] = [[i]]

        rez = []
        for i in hash_table.keys():
            for k in hash_table[i]:
                rez.append(k)

        return rez