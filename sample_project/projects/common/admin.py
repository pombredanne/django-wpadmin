from django.contrib.admin.sites import AdminSite

from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

from django.contrib.sites.models import Site
from django.contrib.sites.admin import SiteAdmin

from authors.models import Author
from authors.admin import AuthorAdmin

from books.models import BookCategory, Book
from books.admin import BookCategoryAdmin, BookAdmin, UserBookAdmin

from cds.models import CdCategory, Cd
from cds.admin import CdCategoryAdmin, CdAdmin, UserCdAdmin

from dvds.models import DvdCategory, Dvd
from dvds.admin import DvdCategoryAdmin, DvdAdmin, UserDvdAdmin

from forms import SuperAdminAuthenticationForm, UserAuthenticationForm


class SuperAdminSite(AdminSite):

    login_form = SuperAdminAuthenticationForm

    def has_permission(self, request):
        """
        Allow only superusers.
        """
        return request.user.is_active and request.user.is_superuser


class UserSite(AdminSite):

    login_form = UserAuthenticationForm

    def has_permission(self, request):
        """
        Allow all users which are in 'users' group.
        """
        return request.user.is_active \
            and request.user.groups.filter(name='users').count()


admin = SuperAdminSite(name='admin')
staff = AdminSite(name='staff')
user = UserSite(name='user')


# admin
admin.register(Site, SiteAdmin)
admin.register(User, UserAdmin)
admin.register(Group, GroupAdmin)

admin.register(Author, AuthorAdmin)
admin.register(BookCategory, BookCategoryAdmin)
admin.register(Book, BookAdmin)
admin.register(CdCategory, CdCategoryAdmin)
admin.register(Cd, CdAdmin)
admin.register(DvdCategory, DvdCategoryAdmin)
admin.register(Dvd, DvdAdmin)

# staff
staff.register(Author, AuthorAdmin)
staff.register(BookCategory, BookCategoryAdmin)
staff.register(CdCategory, CdCategoryAdmin)
staff.register(DvdCategory, DvdCategoryAdmin)

# user
user.register(Book, UserBookAdmin)
user.register(Cd, UserCdAdmin)
user.register(Dvd, UserDvdAdmin)