def stable_match(men_prefs, women_prefs):
    # Initialize all men and women as free
    free_men = list(men_prefs.keys())
    engagements = {}
    # While there are free men
    while free_men:
        man = free_men.pop(0)
        # Get the preferences of the man
        man_pref = men_prefs[man]
        # Propose to the first woman in the man's preference list
        woman = man_pref.pop(0)
        fiance = engagements.get(woman)
        # If the woman is not engaged, engage her with the current man
        if not fiance:
            engagements[woman] = man
        else:
            # If the woman prefers the current man over her fiance
            if women_prefs[woman].index(man) < women_prefs[woman].index(fiance):
                engagements[woman] = man
                free_men.append(fiance)
            else:
                # The woman rejects the proposal
                free_men.append(man)
    return engagements

def get_preferences():
    men_prefs = {}
    women_prefs = {}
    
    num_men = int(input("Enter the number of men: "))
    num_women = int(input("Enter the number of women: "))
    
    print("\nEnter men's preferences:")
    for i in range(num_men):
        man = input(f"Enter name of man {i+1}: ")
        preferences = input(f"Enter {man}'s preferences (comma-separated): ").split(", ")
        men_prefs[man] = preferences
    
    print("\nEnter women's preferences:")
    for i in range(num_women):
        woman = input(f"Enter name of woman {i+1}: ")
        preferences = input(f"Enter {woman}'s preferences (comma-separated): ").split(", ")
        women_prefs[woman] = preferences
    
    return men_prefs, women_prefs

men_prefs, women_prefs = get_preferences()
stable_matches = stable_match(men_prefs, women_prefs)
print("\nStable Marriages:")
for woman, man in stable_matches.items():
    print(f"{man} engaged to {woman}")
