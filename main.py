from CRUD import CRUDCategory

category = CRUDCategory.get(category_id=1)
print(category)
category.name = 'Eда'
CRUDCategory.update(category=category)
print(CRUDCategory.get(category_id=1))