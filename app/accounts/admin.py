# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from django.contrib.auth.models import Group
# # from django.contrib.auth.admin import AccountAdmin as BaseUserAdmin
#
# from .forms import AccountAdminCreationForm, AccountAdminChangeForm
# from .models import Account
# # Register your models here.
#
# Account = get_user_model()
#
# class AccountAdmin(admin.ModelAdmin):
#     search_fields = ['email']
#     form = AccountAdminChangeFrom() # editview
#     add_form = AccountAdminCreation() # create view
#     # class Meta:
#     #     model = Account
#
# admin.site.register(Account, AccountAdmin)
#
# class AccountAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = AccountAdminChangeForm
#     add_form = AccountAdminCreationForm
#
#     # The fields to be used in displaying the Account model.
#     # These override the definitions on the base AccountAdmin
#     # that reference specific fields on auth.Account.
#     list_display = ('email', 'admin')
#     list_filter = ('admin',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ()}),
#         ('Permissions', {'fields': ('admin',)}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. AccountAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()
#
#
# admin.site.register(Account, AccountAdmin)
# admin.site.unregister(Group)
#
# class AccontAdminCreationForm(forms.ModelForm):
#     """A form for creating new accounts. Includes all the required
#     fields, plus a repeated password."""
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = Account
#         fields = ('email', 'full_name')
#
#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         account = super(AccontAdminCreationForm, self).save(commit=False)
#         account.set_password(self.cleaned_data["password1"])
#         if commit:
#             account.save()
#         return account
#
#
# class RegisterForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
#
#     class Meta:
#         model = Account
#         fields = ('email',)
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         qs = Account.objects.filter(email=email)
#         if qs.exists():
#             raise forms.ValidationError("email is taken")
#         return email
#
#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#
#
# class AccontAdminCreationForm(forms.ModelForm):
#     """A form for creating new accounts. Includes all the required
#     fields, plus a repeated password."""
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = Account
#         fields = ('email',)
#
#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         account = super(AccontAdminCreationForm, self).save(commit=False)
#         account.set_password(self.cleaned_data["password1"])
#         if commit:
#             account.save()
#         return account
#
#
# class AccountAdminChangeForm(forms.ModelForm):
#     """A form for updating accounts. Includes all the fields on
#     the account, but replaces the password field with admin's
#     password hash display field.
#     """
#     password = ReadOnlyPasswordHashField()
#
#     class Meta:
#         model = Account
#         fields = ('email', 'full_name', 'password', 'active', 'admin')
#
#     def clean_password(self):
#         # Regardless of what the account provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial["password"]
