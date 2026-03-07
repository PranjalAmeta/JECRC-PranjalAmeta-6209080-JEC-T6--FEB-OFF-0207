import time 
class TODO:
    todos = [
        # {
        #     'id':'',
        #     'desc':'',
        #     'isCompleted':False
        # }
    ]
    def add_todo(self, desc):
        # 1. Take desc from the user
        # 2. We have to create one dict in which we will add todo desc
        # 3. Append the dict inside todo 
        if(len(desc)==0):
            print('Task cannot be empty.')
        else:
            self.todos.append({'id':int(time.time()),'desc':desc,'isCompleted':False})

    
    def remove_todo(self, id):
        flag=False
        for i in self.todos:
            if(i['id']==id):
                print('deleted todo:',i)
                self.todos.remove(i)
                flag=True
        if(flag==False): print('enter a valid id')
    
    def display_todos(self):
        if(len(self.todos)==0): print('no todos to display')
        for i in self.todos:
            print(i)
    
    def update_todo(self, id, new_desc):
        flag=False
        for i in self.todos:
            if(i['id']==id):
                i['desc']=new_desc
                flag=True
                break
        if(flag==False):
            print('Enter a correct id')
    
    def toggle_mark_as_completed(self, id):
        flag=False
        for i in self.todos:
            if(i['id']==id):
                i['isCompleted']=True
                flag=True
                break
        if(flag==False):
            print('Enter a valid id')
    
    def completed_todos(self):
        flag=False
        for i in self.todos:
            if(i['isCompleted']==True):
                flag=True
                print(i)
        if(flag==False):
            print('no completed todos')
    
    def incompleted_todos(self):
        for i in self.todos:
            if(i['isCompleted']==False):
                print(i)


