# from allauth.account.adapter import DefaultAccountAdapter
# from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
# from django.forms import ValidationError
# from django.shortcuts import redirect
# from django.contrib import messages

# class NoNewUsersAccountAdapter(DefaultAccountAdapter):
#     def is_open_for_signup(self, request):
#         raise ValidationError("New account registrations are closed.")

# class NoNewUsersSocialAccountAdapter(DefaultSocialAccountAdapter):
#     def pre_social_login(self, request, sociallogin):
#         if not sociallogin.is_existing:
#             # If the social account is new and does not have an associated user
#             messages.error(request, "New account registrations are closed.")
#             # Redirect to a page where you can display the error message, for example, the login page
#             return redirect("/")

#         # Allow the login to proceed if the account exists
#         return super().pre_social_login(request, sociallogin)