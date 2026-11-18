playlist = ["Flowers", "Blinding Lights", "Shape of You", "Levitating", "Flowers"]

print("===== PLAYLIST MANAGER =====")
print("Playlist: ", playlist)
print("Songs: ", len(playlist))
print("First song", playlist[0])
print("Last song", playlist[-1])

playlist.append("Houdini")
playlist.insert(1, "Calm Down")
print("After adding:", playlist)

playlist.extend(["As it was", "Anti-Her"])
print("Playlist after extending: ", playlist)

flower = "Flowers"
print(f"{flower} Count: {playlist.count(flower)}")

playlist.remove(flower)
print("After remove", playlist)

print(f"Levitating position: {playlist.index('Levitating')}")

if "Despacito" in playlist:
    print("Despacito found: Yes")
else:
    print("Despacito found: No")

skipped_song = playlist.pop()
print("Skipped", skipped_song)

played_song = playlist.pop(0)
print("Now Played", played_song)

playlist.sort()
print("Sorted", playlist)
print("Songs left", len(playlist))
print("============================")
