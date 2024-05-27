# state_management.py
class StateManagement:
    def __init__(self):
        self.state = "awake"  # other states could be "sleep", "curious", "motivated", etc.

    def set_state(self, new_state):
        self.state = new_state

    def get_state(self):
        return self.state

    def update_state_based_on_activity(self, activity_level):
        if activity_level < 0.2:
            self.state = "sleep"
        elif activity_level > 0.8:
            self.state = "curious"
        else:
            self.state = "awake"
