class VerifySchema:
    @staticmethod
    def verify_user_schema(user_schema):
        fields = ['username', 'email', 'name', 'password']
        for field in fields:
            if field not in user_schema.keys():
                message = f"{field} is a required field!"
                return False, message
        return True

    @staticmethod
    def verify_post_schema(post_schema):
        fields = ['title', 'content', 'user_id']
        for field in fields:
            if field not in post_schema.keys():
                message = f"{field} is a required field!"
                return False, message
        return True

    @staticmethod
    def verify_comment_schema(comment_schema):
        fields = ['content', 'post-id', 'user_id']
        for field in fields:
            if field not in comment_schema.keys():
                message = f"{field} is a required field!"
                return False, message
        return True