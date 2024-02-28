from collections import Counter
def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p
    print(dic1)
    print(dic2)
    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        print(k,v)
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            print(i,p)
            answer.append(i)

    return answer
    
#     dic={}
#     phrase={}
#     for index,genre in enumerate(genres):
#         if genre not in dic:
#             dic[genre]=[[plays[index],index]]
#         else:
#             dic[genre].append([plays[index],index])
#     print(dic)
#     for types,count in dic.items():
#         sum=0
#         for x in count:
#             sum+=x[0]
#         if len(count)==1:
#             phrase[sum]=count[:1]
#         else:    
#             phrase[sum]=sorted(count,reverse=True)[:2]
#         sorted_phrase = sorted(phrase.items(), key = lambda item: item[0], reverse = True)
#         print(sorted_phrase)
#         answer=[]
#         for x,counts in sorted_phrase:
#             for y,i in enumerate(counts):
#                 if y==0:
#                     temp=i[0]
#                     temp_index=i[1]
#                 else:
#                     if temp==i[0]:
#                         temp_index>i[1]
#                         answer.pop()
#                         answer.extend([i[1],temp_index])
#                         break
#                 answer.append(i[1])
#     print(answer)            
#     return answer
            
    
    
    
    
    
    
    
    
    
    
