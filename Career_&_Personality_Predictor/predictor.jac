import from byllm { Model}
glob llm = Model(model_name ="gemini/gemini-2.0-flash")

"""Represents a user's personal and skill profile"""
obj Profile{
    has name: str;
    has age: int;
    has interests: list[str];
    has skills: list[str];
    has personality_type: list[str];
}

""" Gives more context about the user profile to the llm"""
sem Profile.name = "The full name of the person";
sem Profile.age = "The age of the person in years";
sem Profile.interests = "A list of the person's interests and hobbies";
sem Profile.skills = "A list of the person's professional skills";
sem Profile.personality_type = "A list of personality traits based on common frameworks like MBTI or Big Five";

"""Suggests career paths and learning directions based on the profile"""
def suggest_career(profile: Profile) -> list[str] by llm();

"""Gives advice on next learning steps based on career suggestion"""
def learning_path(profile: Profile, chosen_career: str) -> str by llm();