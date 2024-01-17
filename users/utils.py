# def register_confirm(request, user):
#     current_site = get_current_site(request)
#     context = {
#         "user": user,
#         "domain": current_site.domain,
#         "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#         "token": user.user_token,
#     }
#
#
#     message = f'http://{current_site}/users/verify_email/{context["uid"]}/{context["token"]}/'
#     data = {
#         'current_site': current_site,
#         'context': context,
#         'message': message,
#     }
#     return data
