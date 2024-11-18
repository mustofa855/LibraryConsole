# copy dictionary

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasep",
    "cuy":"ucuy surucuy"
}

friends = teman_teman.copy()
# friends = teman_teman

print(f"teman-teman = {teman_teman}\n")
print(f"friends = {friends}\n")

teman_teman["cup"]="ucup si keren"
print(f"teman-teman = {teman_teman}\n")
print(f"friends = {friends}\n")

# pop dictionary (ambil berdasarkan key)
dataAsep = friends.pop("sep")
print(f"Data asep = {dataAsep}\n")
print(f"friends = {friends}\n")

# popitem dictionary (yang terakhir aja)
dataTerakhir = friends.popitem()
print(f"Data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")