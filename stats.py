def word_count(src)->int:
    return len(src.split())

def char_count(src)->dict[str,int]:
    d={}
    for char in src:
        c=char.lower()
        if c in d:
            d[c]+=1
        else:
            d[c]=1
    return d
def sort_on(my_tuple:tuple[str,int])->int:
    return my_tuple[1]

def chars_dict_to_sorted_list(my_dict)->list[tuple[str,int]]:
    my_list=[]
    for keys in my_dict:
        count=my_dict[keys]
        my_list.append((keys,count))
    sorted_list=sorted(my_list,reverse=True,key=sort_on)
    return sorted_list
