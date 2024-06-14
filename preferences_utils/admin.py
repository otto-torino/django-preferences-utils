from django.contrib import admin
from django.http.request import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

csrf_protect_m = method_decorator(csrf_protect)


class PreferencesUtilsAdmin(admin.ModelAdmin):
    # override to change submit row
    change_form_template = "admin/preferences_utils/change_form.html"

    @csrf_protect_m
    def changelist_view(self, request: HttpRequest, extra_context=None):
        """
        Display single preferences object as a readonly changeform
        """
        model = self.model
        obj = model.instance()
        return redirect(
            "%s?readonly=1" # readonly to have a view object
            % reverse(
                "admin:%s_%s_change" % (model._meta.app_label, model._meta.model_name),
                args=(obj.id,),
            )
        )

    def has_change_permission(self, request, obj=None):
        return request.GET.get("readonly") != "1"

    def has_add_permission(self, request: HttpRequest):
        return False
