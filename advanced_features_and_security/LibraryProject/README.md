# permissions setup:
# - can_view: allows user to see book list
# - can_create: allows user to create new book entries
# - can_edit: allows user to edit existing book entries
# - can_delete: allows user to delete book entries
#
# Groups:
# - Viewers: only can_view
# - Editors: can_view, can_create, can_edit
# - Admins: full access
# CSRF_COOKIE_SECURE ensures the CSRF cookie is only sent via HTTPS
# SECURE_CONTENT_TYPE_NOSNIFF stops the browser from guessing MIME types
# Always validate form input to prevent XSS and injection
# Using ORM prevents SQL injection attacks
