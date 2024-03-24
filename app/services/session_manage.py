import random
import string

class Session_Manager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user):
        session_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        self.sessions[session_id] = user
        return session_id

    def get_user(self, session_id):
        return self.sessions.get(session_id)

    def delete_session(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]

    def get_user_sessions(self, user):
        return [session_id for session_id, session_user in self.sessions.items() if session_user == user]

session_manager = Session_Manager()
