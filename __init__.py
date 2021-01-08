from mycroft import MycroftSkill, intent_file_handler


class TestingSkills(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skills.testing.intent')
    def handle_skills_testing(self, message):
        self.speak_dialog('skills.testing')


def create_skill():
    return TestingSkills()

