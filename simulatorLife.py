#Beta 0.0.1
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

causes_of_death = [
    'Natural causes',
    'Accident',
    'Illness',
    'Old age',
    'Unknown',
    'Flu',
    'Cold',
    'COVID-19'
]

def ask_question():
    global player_age, player_health
    options = age_categories[player_age]
    
    if player_health <= 50:
        print("You don't feel well today.")
        available_choices = [option for option in options if option not in diseases.keys()]
        options = available_choices
    
    random_choices = random.sample(options, k=2)
    print(f"What would you like to do today? {random_choices[0]} or {random_choices[1]}")
    player_input = input("Enter your choice: ")
    
    if player_input in diseases.keys():
        player_health -= diseases[player_input]['health_loss']
        options.remove(player_input)
        print(diseases[player_input]['effect'])
        
        death_chance = diseases[player_input]['death_chance']
        if random.random() < death_chance:
            cause_of_death = player_input
            return True, cause_of_death
    else:
        player_health -= 10
        
    if player_health <= 0:
        cause_of_death = random.choice(causes_of_death)
        return True, cause_of_death
    else:
        player_age += 1
        if player_age in chance_of_death.keys() and random.random() < chance_of_death[player_age]:
            cause_of_death = random.choice(causes_of_death)
            return True, cause_of_death
        elif player_age == 110:
            return True, "You have reached the age of 110. Congratulations, you win!"
        else:
            return False, None
def start_game():
    global player_age, player_health

    player_age = 0
    player_health = 100

    while player_age < 110:
        if player_age == 110:
            print("Congratulations! You have reached the age of 110. You win!")
            break

        print(f"At age {player_age}, your options are: {age_categories[player_age]}")
        choice = input("Enter the number of your choice (1-3): ")

        while choice not in ["1", "2", "3"]:
            print("Invalid choice. Please choose again.")
            choice = input("Enter the number of your choice (1-3): ")

        choice = int(choice) - 1

        if choice >= len(age_categories[player_age]):
            print("Invalid choice. Please choose again.")
            continue

        selected_option = age_categories[player_age][choice]
        if selected_option in diseases.keys():
            player_health -= diseases[selected_option]['health_loss']
            print(diseases[selected_option]['effect'])
            if random.random() < diseases[selected_option]['death_chance']:
                cause_of_death = selected_option
                print("Game over. You have died.")
                print(f"Cause of death: {cause_of_death}")
                break
        else:
            player_health -= 10

        if player_health <= 0:
            cause_of_death = random.choice(causes_of_death)
            print("Game over. You have died.")
            print(f"Cause of death: {cause_of_death}")
            break

        player_age += 1

start_game()

