
def in_proj_user_group(user):
  if user:
    return user.groups.filter(name='project_user').count() > 0
  return False
