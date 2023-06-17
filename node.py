class Node:
    def __init__(self, exp):
        self.exp = exp

    def build_tree(self):
        length = len(self.exp)
        print("exp:", self.exp)

        if length == 1:
            self.node_0 = Node(self.exp)
            return

        i = 0
        while True:
            if self.exp[i] == "(":
                while self.exp[i] != ")":
                    i += 1

            if self.exp[i] == "+":
                self.node_0 = Node(self.exp[:i])
                self.node_1 = Node(self.exp[i + 1 :])
                self.operator = "+"
                self.node_0.build_tree()
                self.node_1.build_tree()
            i += 1
            if i >= length:
                break
        i = 0
        while True:
            if self.exp[i] == "(":

                while self.exp[i] != ")":
                    i += 1

            if self.exp[i] == "•":
                self.node_0 = Node(self.exp[:i])
                self.node_1 = Node(self.exp[i + 1 :])
                self.operator = "•"
                self.node_0.build_tree()
                self.node_1.build_tree()
            i += 1
            if i >= length:
                break
        i = 0
        while True:
            if self.exp[i] == "(":

                while self.exp[i] != ")":
                    i += 1

            if self.exp[i] == "*":
                self.node_0 = Node(self.exp[:i])
                self.operator = "*"
                self.node_0.build_tree()
            i += 1
            if i >= length:
                break
        i = 0
        while True:
            if self.exp[i] == "(":

                while self.exp[i] != ")":
                    i += 1

            if self.exp[i] == ")":
                self.node_0 = Node(self.exp[1 : length - 1])
            i += 1
            if i >= length:
                break
        # print("start build tree...")

        # length = len(self.exp)
        # print("exp:", self.exp)
        # if length == 1:
        #     self.node_0 = Node(self.exp)
        #     return
        # i = 0
        # while True:
        #     print("i:", i)
        #     if self.exp[i] == "(":
        #
        #         while self.exp[i] != ")":
        #             i += 1
        #
        #     if self.exp[i] == "+":
        #         self.node_0 = Node(self.exp[:i])
        #         self.node_1 = Node(self.exp[i + 1 :])
        #         self.operator = "+"
        #         self.node_0.build_tree()
        #         self.node_1.build_tree()
        #     elif self.exp[i] == "•":
        #         print("dot found")
        #         self.node_0 = Node(self.exp[:i])
        #         self.node_1 = Node(self.exp[i + 1 :])
        #         self.operator = "•"
        #         self.node_0.build_tree()
        #         self.node_1.build_tree()
        #     elif self.exp[i] == "*":
        #         self.node_0 = Node(self.exp[:i])
        #         self.operator = "*"
        #         self.node_0.build_tree()
        #     if self.exp[i] == ")":
        #         self.node_0 = Node(self.exp[1 : length - 1])
        #     i += 1

    def print_tree(self):
        self.node_0.print_tree()
        if self.operator:
            print(self.operator)
        if self.node_1:
            self.node_1.print_tree()
