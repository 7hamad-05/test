import pickle 

object = {"name":"hamad", "age":"21", "nationality":"Saudi Arabia"}

serilized = pickle.dumps(object)


print("serilized :", serilized)

unserilized = pickle.loads(serilized)

print("unserilized :", unserilized)