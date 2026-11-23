from pyscript import document

facts = [
    "Fun Fact #1: I was born on January 23, 2011",
    "Fun Fact #2: My favorite artist is Kendrick Lamar, and SAMIMDOT or Prayer (unreleased) is his best works.",
    "Fun Fact #3: The games I only will play are God of War: Ragnarok, Hollow Knight, Minecraft, and Genshin Impact",
    "Fun Fact #4: I'm the eldest amongst' all three of my siblings."
]

current_index = 0

def show_fact(e):
    global current_index
    output = document.getElementById("creator_output")
    output.innerHTML = f"<strong>{facts[current_index]}</strong>"
    current_index = (current_index + 1) % len(facts)
