class Relation:
    def __init__(self,size):
        self.size = size
        self.answer_relation = [0] *3

    def build_matrix(self):
        arr = [list(map(int, input().split())) for i in range(self.size)]
        return arr
    def reflexive_relation(self,arr):
        for i in range(self.size):
            if arr[i][i] == 0:
                self.answer_relation[0]=0
                return 0
        self.answer_relation[0]=1
        return 1
    def symmetrical_relationship(self,arr):
        for i in range(self.size):
            for j in range(self.size):
                if arr[i][j]:
                    if arr[j][i] ==0:
                        self.answer_relation[1] = 0
                        return 0
        self.answer_relation[1] = 1
        return 1
    def transitive_relation(self,arr):
        new_arr = [[0 for _ in range(self.size)]for i in range(self.size)] #R^2
        for i in range(self.size):
            for j in range(self.size):
                for z in range(self.size):
                    new_arr[i][j] += arr[i][z] * arr[z][j]
                if new_arr[i][j]:
                    new_arr[i][j] =1

        for i in range(self.size):
            for j in range(self.size):
                if new_arr[i][j]:
                    if arr[i][j] == 0:
                        self.answer_relation[2]=0
                        return 0
        self.answer_relation[2]=1
        return 1

    def equivalence_relation(self,arr):
        if self.reflexive_relation(arr) and self.symmetrical_relationship(arr) and self.transitive_relation(arr):
            print("이 관계는 동치 관계가 맞습니다.")
            self.equivalence_class(arr)
        else:
            print("이 관계는 동치 관계가 아닙니다.")
            if self.reflexive_relation(arr)==0:
                print("반사 관계가 아닙니다.")
                arr =self.reflexive_closure(arr)
            elif self.symmetrical_relationship(arr)==0:
                print("대칭 관계가 아닙니다")
                arr = self.symmetry_closure(arr)
            elif self.transitive_relation(arr)==0:
                print("추이 관계가 아닙니다.")
                print("추이 폐포 변환 전")
                self.matrixout(arr)
                arr = self.transitive_closure(arr)
                print("추이 폐포 변환 후")
                self.matrixout(arr)
            self.equivalence_relation(arr)

    def equivalence_class(self,arr):
        answer = [[] for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                if arr[i][j]:
                    answer[i].append((i+1,j+1))
        for i in range(self.size):
            if answer[i]:
                print(f"[{i+1}] = ","{ " ,end="")
                for j in range(len(answer[i])):
                    if j == len(answer[i])-1:
                        print(answer[i][j][1],end="")
                    else:
                        print(answer[i][j][1],end=",")
                print(" }")
            else:
                print(f"[{i+1}] = ", "{}")
    def reflexive_closure(self,arr):
        print("반사 폐포 변환 전")
        self.matrixout(arr)
        for i in range(self.size):
            if arr[i][i] == 0:
               arr[i][i] = 1
        print("반사 폐포 변환 후")
        self.matrixout(arr)
        return arr
    def matrixout(self,arr):
        size = len(arr)
        print("┌" + "       " * size + "┐")
        for i in range(size):
            print("│", end="")
            for j in range(size):
                print("%7d" % arr[i][j], end="")
            print("│")
        print("└" + "       " * size + "┘")
    def symmetry_closure(self,arr):
        print("대칭 폐포 변환 전")
        self.matrixout(arr)
        for i in range(self.size):
            for j in range(self.size):
                if arr[i][j]  ==1:
                    arr[j][i] =1
        print("대칭 폐포 변환 후")
        self.matrixout(arr)
        return arr
    def transitive_closure(self,arr):
        for i in range(self.size):
            for j in range(self.size):
               if arr[i][j] == 1:
                   for z in range(self.size):
                       if arr[j][z] ==1:
                           arr[i][z] =1
        if self.transitive_relation(arr):
            return arr
        else:
            self.transitive_closure(arr)
if __name__ =="__main__":
    n = 5
    r1 = Relation(5)
    arr = r1.build_matrix()
    r1.equivalence_relation(arr)
