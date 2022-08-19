

class cart():

    def user_choice(self):        
        self.usr_input_global = []
        self.user_ch =  int(input("1: Add items in the list\n2: Delete item in the list\n3: see your current shopping list\n4: quit\n"))
        if self.user_ch == 1:
            self.add_items()
        elif self.user_ch == 2:
            self.del_items()
        elif self.user_ch == 3:
            self.current_items()
        elif self.user_ch == 4:
            self.program_quit()
        else:
            print("Wrong selection please choose a correct option")
            self.user_choice()

    def add_items(self):
        self.user_input = str(input("enter your list items seperated by comma(,):  "))
        self.list_of_user_input = self.user_input.split(",")
        for self.x in self.list_of_user_input:
            self.usr_input_global.append(self.x)
        print(self.usr_input_global,end="\n")

        self.user_choice()


    def del_items(self):
        self.del_option = str(input("for clearing the list write clear: "))
        if self.del_option == 'clear':
            self.usr_input_global.clear()
        self.user_choice()


    def current_items(self):
        # for self.z in self.usr_input_global:      
        #     print(self.z)                         for some reason the for loop does not work but for now i print the list it self    
        print(self.usr_input_global)
        self.user_choice()
        

    def program_quit(self):
        for self.g in self.usr_input_global:
            print(self.g)
        quit()


        


obj = cart()
obj.user_choice()

