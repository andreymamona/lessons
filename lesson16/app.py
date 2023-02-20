import requests


# r = requests.get("http://127.0.0.1:5000/", params={"title": "test"})
# print(r.content)
#
# r = requests.get("http://127.0.0.1:5000/test")
# print(r.json())
# print(r.status_code)

# r = requests.get("http://127.0.0.1:5000/users")
# print(r.json())


r = requests.post("http://127.0.0.1:5000/test", data={
   "email": "test1@test.tst",
   "password": "test",
   "phone": "+375-29-1010101",
   "age": "99",
   "city": "Test",
   "address": "Test",
})
print(r.status_code)

