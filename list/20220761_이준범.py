class Node:
    def __init__(self, elem, next = None):
        self.elem = elem
        self.link = next
    
    def append(self, new): # 새로운 노드를 뒤에 삽입
        if new is not None:
            new.link = self.link
            self.link = new

    def popNext(self): # 다음 노드를 삭제하고 반환
        deleted = self.link
        
        if self.link is not None:
            self.link = deleted.link
            return deleted

class LinkedList: # 단순 연결 리스트 클래스
    def __init__(self):
        self.head = None

    def is_empty(self): # 비어있는지 검사
        return self.head is None
    
    def getNode(self, pos): # pos번째에 있는 노드를 반환
        if pos < 0:
            return None
        prt = self.head
        for n in range(pos):
            if prt == None:
                return None
            prt = prt.link
        return prt
    
    def insert(self, book):  # 리스트 새로운 노드 추가
        node = Node(book)
        if self.head is None: # 리스트가 비어있는 경우
            self.head = node
        else: # 리스트가 비어있지 않은 경우
            ptr = self.head
            while ptr.link is not None:
                ptr = ptr.link
            ptr.link = node

    def delete(self, pos): # 리스트에 pos 위치에 있는 노드 삭제
        if pos < 0 :
            raise IndexError("empty 또는 범위 밖 오류")
        
        before = self.getNode(pos-1) # 1. 삭제할 노드 이전 노드
        # 2. before 노드의 위치에 따라 구분
        if before is None:
            if pos == 0 : # 머리 노드 삭제
                deleted = self.head
                self.head = deleted.link
                deleted.link = None # 연결 해제
                return deleted
            else: # 2) pos가 리스트 밖에 있는 경우
                return IndexError("empty 또는 범위 밖 오류")
        else:     
            before.popNext() # 3) 중간 노드 삭제

    
    def display(self, msg="LinkedList:"): # 리스트의 내용물 번호순으로 출력
        print(msg, end = ' ')
        ptr = self.head
        while ptr is not None:
            
            print(f"책 번호:{ptr.elem.book_id}, 제목:{ptr.elem.title}", end = " -> ")
            ptr = ptr.link
            if self.head is None:
                return
        print("책이 없습니다")

    def find_by_title(self, title): # 책 제목으로 리스트에서 도서를 찾기
        ptr = self.head
        while ptr is not None:
            if ptr.elem.title == title:
                return ptr
            ptr = ptr.link
        return None
        
    def find_pos_by_title(self, title): # 책 제목을 기반으로 리스트에서 위치찾기
        ptr = self.head
        pos = 0
        while ptr is not None:
            if ptr.elem.title == title:
                return pos
            ptr = ptr.link
            pos += 1
        return None
    
class Book:
    def __init__(self, book_id, title, author, year): # 책 정보
        self.title = title
        self.author = author
        self.book_id = book_id
        self.year = year

class BookManagement: # 도서 관리 클래스
    def __init__(self):
        self.list = LinkedList()
    
    def add_book(self, book_id, title, author, pub_year): # 책를 리스트에 추가
        ptr = self.list.head
        while ptr is not None:
            if ptr.elem.book_id == book_id:   # 중복된 책 번호 검사
                print(f"{book_id}번 책이 이미 존재합니다.\n")
                return False
            ptr = ptr.link
        
        book = Book(book_id, title, author, pub_year)
        self.list.insert(book)
        print(f"'{title}' 도서가 추가되었습니다.\n")
        return True
    
    def remove_book(self, title): # 책제목에 해당하는 도서를 리스트에서 삭제
        pos = self.list.find_pos_by_title(title) # 책 제목으로 위치 찾기
        if pos is not None:
            self.list.delete(pos) # 삭제
            return True
        else:
            return False
    
    def search_book(self, title): # 책제목에 해당하는 도서를 리스트에서 찾기
        node = self.list.find_by_title(title)
        if node is not None:
            return node.elem
        else:
            return None

    def display_books(self): # 전체 도서 목록 출력
        self.list.display("도서 목록:")
        
    def run(self): # 도서 관리 프로그램 실행

    
        while True:
            print("=== 도서관리 프로그램 === \n")
            print("1) 도서추가\n")
            print("2) 도서 삭제 (책 제목으로 삭제) \n")
            print("3) 도서 조회 (책 제목으로 조회) \n")
            print("4) 전체 도서 목록 출력 \n")
            print("5) 종료.\n")
        
            choice = input("메뉴를 선택하세요: ").strip()    

            if choice == '5':
                print("프로그램을 종료합니다.")
                break
            
            elif choice not in ['1', '2', '3', '4']:
                print("1,2,3,4,5 중에서 선택하세요. \n")
                continue
            
            elif choice == '1':
                print("도서 추가 \n")
                book_id = input("책 번호(숫자): ").strip()
                if not book_id.isdigit():
                    print("책 번호는 숫자여야 합니다.\n")
                    continue
                title = input("책 제목: ").strip()
                author = input("저자: ").strip()
                pub_year = input("출판 년도: ").strip()
                if not pub_year.isdigit():
                    print("출판 년도는 숫자여야 합니다.\n")
                    continue
                self.add_book(book_id, title, author, pub_year)
            
            elif choice == '2':
                print("삭제할 책 제목을 입력하세요: ")
                title = input().strip()
                if self.remove_book(title):
                    print(f"'{title}' 도서가 삭제되었습니다.\n")
                else:
                    print(f"'{title}' 도서를 찾을 수 없습니다.\n")

            elif choice == '3':
                print("조회할 책 제목을 입력하세요: ")
                title = input().strip()
                book = self.search_book(title)
                if book is not None:
                    print(f"도서 정보 제목: 번호: {book.book_id}{book.title}, 저자: {book.author}, 출간년도: {book.year}\n")
                else:
                    print(f"'{title}' 도서를 찾을 수 없습니다.\n")

            elif choice == '4':
                self.display_books()

if __name__ == "__main__":
    BookManagement().run()
