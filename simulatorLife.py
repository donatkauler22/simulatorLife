#Beta 4.1.6
#Creators: Donat, Lev, Georg
import random
import time

player_age = 0
player_health = 100

age_categories = {
    0: ['Cry', 'Sleep', 'Eat'],
    1: ['Play', 'Learn', 'Explore'],
    2: ['Make friends', 'Start school', 'Discover hobbies'],
    3: ['Go to preschool', 'Learn basic skills', 'Play with other kids'],
    4: ['Continue learning', 'Develop social skills', 'Explore interests'],
    5: ['Choose a favorite subject', 'Join a sports team', 'Attend birthday parties'],
    6: ['Advance academic skills', 'Develop hobbies', 'Build friendships'],
    7: ['Explore new activities', 'Join clubs', 'Learn new skills'],
    8: ['Expand knowledge', 'Participate in competitions', 'Develop independence'],
    9: ['Prepare for middle school', 'Join extracurricular activities', 'Deepen friendships'],
    10: ['Choose a favorite sport', 'Develop study habits', 'Join a club'],
    11: ['Transition to middle school', 'Explore different subjects', 'Form new friendships'],
    12: ['Prepare for high school', 'Pursue interests', 'Set goals'],
    13: ['Adapt to high school', 'Explore career options', 'Develop personal identity'],
    14: ['Choose extracurricular activities', 'Prepare for college', 'Build support networks'],
    15: ['Choose a favorite hobby', 'Think about college', 'Get a part-time job'],
    16: ['Explore potential careers', 'Start building a resume', 'Prepare for driver\'s license'],
    17: ['Plan for college applications', 'Consider higher education options', 'Develop financial literacy'],
    18: ['Choose a college major', 'Think about career goals', 'Start dating'],
    19: ['Navigate college life', 'Expand social circles', 'Network for future opportunities'],
    20: ['Focus on academic goals', 'Build professional skills', 'Consider internships'],
    21: ['Graduate from college', 'Transition to adult life', 'Make important life decisions'],
    22: ['Enter the workforce', 'Continue education', 'Adjust to post-college life'],
    23: ['Build professional experience', 'Establish financial stability', 'Pursue personal growth'],
    24: ['Explore different paths', 'Embrace new opportunities', 'Forge long-lasting connections'],
    25: ['Choose a career path', 'Think about long-term goals', 'Find a partner'],
    30: ['Advance in career', 'Consider starting a family', 'Invest for the future'],
    35: ['Think about starting a family', 'Develop a savings plan', 'Pursue hobbies'],
    40: ['Balance work and family', 'Plan for children\'s education', 'Maintain physical and mental well-being'],
    45: ['Reflect on life choices', 'Prepare for midlife changes', 'Strengthen relationships'],
    50: ['Plan for retirement', 'Travel to new places', 'Spend time with family'],
    55: ['Transition to retirement', 'Pursue personal interests', 'Focus on health and wellness'],
    60: ['Enjoy retirement activities', 'Spend time with grandchildren', 'Engage in lifelong learning'],
    65: ['Enjoy retirement', 'Stay active and healthy', 'Spend time with grandchildren'],
    70: ['Embrace senior living', 'Engage in leisure activities', 'Reflect on life experiences'],
    80: ['Enjoy golden years', 'Spend time with loved ones', 'Maintain overall well-being'],
    90: ['Celebrate a life well-lived', 'Share wisdom with others', 'Enjoy peaceful moments'],
    100: ['Achieve centenarian status', 'Celebrate milestones', 'Be an inspiration to others'],
    110: ['Congratulations! You have reached the age of 110. You win!']
}


diseases = {
    'Flu': {
        'effect': 'You feel sick and can only choose one activity today.',
        'health_loss': 10,
        'choice_loss': 1,
        'death_chance': 0.05
    },
    'Cold': {
        'effect': 'You have a runny nose and can only choose one activity today.',
        'health_loss': 5,
        'choice_loss': 1,
        'death_chance': 0.02
    },
    'COVID-19': {
        'effect': 'You have COVID-19 and must rest today.',
        'health_loss': 25,
        'choice_loss': 2,
        'death_chance': 0.1
    }
}
age_death_chances = {
    30: 0.1,
    40: 0.2,
    50: 0.3,
    60: 0.4,
    70: 0.5,
    80: 0.6,
    90: 0.7,
    100: 0.8,
    110: 1.0
}




causes_of_death = [
    "You succumbed to a disease.",
    "You had a fatal accident.",
    "Your health deteriorated rapidly.",
]

diseases = {
    "Common Cold": {
        "effect": "You caught a cold. Take rest and drink fluids.",
        "health_loss": 10,
        "death_chance": 0.05,
    },
    "Influenza": {
        "effect": "You got the flu. Take medications and stay hydrated.",
        "health_loss": 20,
        "death_chance": 0.1,
    },
    "Pneumonia": {
        "effect": "You contracted pneumonia. Seek medical attention immediately.",
        "health_loss": 30,
        "death_chance": 0.2,
    },
}

def ask_question():
    global player_age, player_health

    options = age_categories[player_age]

    if player_health <= 50:
        print("You don't feel well today.")
        available_choices = [option for option in options if option not in diseases.keys()]
        options = available_choices

    print(f"\nCurrent Age: {player_age} years")
    print(f"Health: {player_health}%")

    print("\nWhat would you like to do today?")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    player_input = input("Enter your choice (1, 2, or 3): ")

    if player_input not in ["1", "2", "3"]:
        print("Invalid choice. Please select a valid option.")
        return ask_question()

    player_choice = options[int(player_input) - 1]

    if player_choice in diseases.keys():
        player_health -= diseases[player_choice]['health_loss']
        options.remove(player_choice)
        print(diseases[player_choice]['effect'])

        if player_health <= 0:
            cause_of_death = "Your health dropped to zero."
            return True, cause_of_death
        elif random.random() < diseases[player_choice]['death_chance']:
            cause_of_death = diseases[player_choice]['effect']
            return True, cause_of_death
        else:
            print("You survived the illness.")

    else:
        player_health += 10

    if player_health > 100:
        player_health = 100

    if player_health <= 0:
        cause_of_death = "Your health dropped to zero."
        return True, cause_of_death

    else:
        if player_age >= 110:
            return True, "You have reached the age of 110"

        if player_age in age_death_chances.keys():
            if random.random() < age_death_chances[player_age]:
                return True, "You died of old age."

        if player_age >= 70 and player_age % 10 == 0:
            player_age += 10  # Add 10 years to the player's age
        elif player_age >= 25 and player_age % 5 == 0:
            player_age += 5  # Add 5 years to the player's age
        else:
            player_age += 1

    return False, None






def start_game():
    global player_age, player_health

    print("Welcome to the Life Simulator!")
    print("You will make choices that affect your health and lifespan.")
    print("Let's begin.")

    player_age = 0
    player_health = 100

    game_over = False
    cause_of_death = None

    while not game_over:
        game_over, cause_of_death = ask_question()

    print(f"\nGame Over. {cause_of_death}")
    print("Thank you for playing the Life Simulator!")

start_game()





input()
