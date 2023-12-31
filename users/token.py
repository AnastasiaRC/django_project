from django.contrib.auth.tokens import PasswordResetTokenGenerator


class EmailVerificationTokenGenerator(PasswordResetTokenGenerator):
    """Создание токена для верификации по почте"""
    def _make_hash_value(self, user, timestamp):
        return (
                str(user.is_active) + str(user.pk) + str(timestamp)
        )


email_verification_token = EmailVerificationTokenGenerator()
