from CRUD import CRUDCategory
from CRUD import CRUDUser

#category = CRUDCategory.get(category_id=1)
#print(category)
#category.name = 'Eда'
#category.parent_id = None
#CRUDCategory.update(category=category)
#print(CRUDCategory.get(category_id=1))

CRUDUser.add(username="Vasya", hashed_password="lsanlda", email='vasya@gmail.com', is_blocked=False)
CRUDUser.add(username="Gena", hashed_password="lsanldcsa", email='gena@gmail.com', is_blocked=False)
CRUDUser.add(username="Petya", hashed_password="lda", email='petya@gmail.com', is_blocked=True)
CRUDUser.add(username="Vanya", hashed_password="lswdqlda", email='vanya@gmail.com', is_blocked=False)
