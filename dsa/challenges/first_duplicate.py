import array

nums = array.array('i', [10,20,13,14,15,13,17,10,20,13])

def find_duplicate():
    st = set()
    for num in nums:
        if num in st:
            return num
        else:
            st.add(num)
    return -1

print(find_duplicate())