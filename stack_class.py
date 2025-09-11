# define stack class with push, pop, peek, is_empty, and size methods
# Stack ADT
class ArrayStack :
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] *capacity
        self.top = -1
    def is_empty(self) :
        return self.top == -1
    def is_full(self) : 
        return self.top == self.capacity - 1
    def push(self, item):
        if not self.is_full():
            self.top = self.top + 1
            self.array[self.top] = item
            #print(f"PUSH: {item!r} stack is now {self.array[:self.top +1]}")
        else :
            raise OverflowError("Stack Overflow") # pass
    def pop(self) :
        if not self.is_empty():
            item = self.array[self.top]
            self.array[self.top] = None
            self.top -= 1
            #print(f"POP : {item!r} -> stack is now {self.array[:self.top +1]}")
            return item
        else:
            return IndexError("Stack underflow")
    def reverse(self, re):
        if not self.is_empty():
            item = self.pop()         
            re.push(item)              
            print(f"reverse : {item!r} -> stack is now {re.array[:re.top +1]}")
            return item
        else:
            return IndexError("Stack underflow")
    def peek(self):
        if not self.is_empty():
            return self.array[self.top]
        return None
    def size(self):
        return self.top+1

# Test the stack class
def reverse_string(statement):
    print("\n[1] PUSH 단계 -----------------------")
    st = ArrayStack(len(statement))
    for char in statement:
        st.push(char)
    re = ArrayStack(len(statement))
    print("\n[2] reverse 단계--------------------------------------")
    out = [] #list
    while not st.is_empty():
        st.reverse(re)

#    print("\n[2] POP 단계--------------------------------------")
#    out = [] #list
#    while not st.is_empty():
#        out.append(st.reverse())

    result = ''.join(re.array[:re.size()])
    print(f"\n[3] 최종 결과: {result}")
    return result

if __name__ == "__main__":
    statement = "안녕하세요, 반갑습니다!"
    reverse_string(statement)
