# looping dictionary

teman_teman = {
	"cup":"ucup surucup",
	"tong":"otong surotong",
	"dung":"dudung surudung",
	"sep":"asep si kasyep",
	"cuy":"ucuy surucuy"
}

# looping first try (yang keluar adalah keynya)

for teman in teman_teman:
	print(teman)

print("="*20, "\n\n")

# operator untuk mengambil item / iterables
keys = teman_teman.keys()
print(keys)
print("="*20)

for key in teman_teman.keys():
	print(teman_teman.get(key))


print("="*20, "\n\n")


values = teman_teman.values()
print(values)
print("="*20)

for value in teman_teman.values():
	print(value)

print("="*20, "\n\n")


items = teman_teman.items()
print(items)
print("="*20)

for item in teman_teman.items():
	print(item)
 

print("="*20, "\n\n")


for key,value in teman_teman.items():
	print(f"key = {key}, value = {value}")