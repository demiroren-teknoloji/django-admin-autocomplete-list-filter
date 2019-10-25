# pylint: disable=R0903,R0913,R0201

import sys
import warnings

from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelect
from django.db.models.fields.related_descriptors import (
    ManyToManyDescriptor,
    ReverseManyToOneDescriptor,
)
from django.utils.translation import ugettext_lazy as _

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON_FOR_FSTRING = (3, 6)
USE_FSTRING = CURRENT_PYTHON >= REQUIRED_PYTHON_FOR_FSTRING


class WillRemoveInVersion10(FutureWarning):
    pass


class AjaxAutocompleteSelectWidget(AutocompleteSelect):
    def __init__(self, *args, **kwargs):
        self.qs_target_value = kwargs.pop('qs_target_value')
        self.model_admin = kwargs.pop('model_admin')
        self.model = kwargs.pop('model')
        self.field_name = kwargs.pop('field_name')
        kwargs.update(admin_site=self.model_admin.admin_site)
        kwargs.update(rel=getattr(self.model, self.field_name).field.remote_field)
        super().__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, renderer=None):
        rendered = super().render(name, value, attrs, renderer)

        if not USE_FSTRING:
            warnings.warn('Will remove str.format, will use f-strings only', WillRemoveInVersion10)
        html_string = (
            '<div class="ajax-autocomplete-select-widget-wrapper" data-qs-target-value="{qs_target_value}">'
            '{rendered}'
            '</div>'
        ).format(qs_target_value=self.qs_target_value, rendered=rendered)
        return html_string


class AjaxAutocompleteListFilter(admin.RelatedFieldListFilter):
    title = _('list filter')
    parameter_name = '%s__%s__exact'
    template = 'djaa_list_filter/admin/filter/autocomplete_list_filter.html'

    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)

        qs_target_value = self.parameter_name % (field.name, model._meta.pk.name)
        queryset = self.get_queryset_for_field(model, field.name)
        widget = AjaxAutocompleteSelectWidget(
            model_admin=model_admin, model=model, field_name=field.name, qs_target_value=qs_target_value
        )

        class AutocompleteForm(forms.Form):
            autocomplete_field = forms.ModelChoiceField(queryset=queryset, widget=widget, required=False)
            querystring_value = forms.CharField(widget=forms.HiddenInput())

        autocomplete_field_initial_value = request.GET.get(qs_target_value, None)
        initial_values = dict(querystring_value=request.GET.urlencode())
        if autocomplete_field_initial_value:
            initial_values.update(autocomplete_field=autocomplete_field_initial_value)
        self.autocomplete_form = AutocompleteForm(initial=initial_values)

    def get_queryset_for_field(self, model, name):
        """
        Thanks to farhan0581
        https://github.com/farhan0581/django-admin-autocomplete-filter/blob/master/admin_auto_filters/filters.py
        """

        field_desc = getattr(model, name)
        if isinstance(field_desc, ManyToManyDescriptor):
            related_model = field_desc.rel.related_model if field_desc.reverse else field_desc.rel.model
        elif isinstance(field_desc, ReverseManyToOneDescriptor):
            related_model = field_desc.rel.related_model
        else:
            return field_desc.get_queryset()
        return related_model.objects.get_queryset()


class AjaxAutocompleteListFilterModelAdmin(admin.ModelAdmin):
    def get_list_filter(self, request):
        list_filter = list(super().get_list_filter(request))
        autocomplete_list_filter = self.get_autocomplete_list_filter()
        if autocomplete_list_filter:
            for field in autocomplete_list_filter:
                list_filter.append((field, AjaxAutocompleteListFilter))
        return list_filter

    def get_autocomplete_list_filter(self):
        return list(getattr(self, 'autocomplete_list_filter', []))

    class Media:
        js = [
            'admin/js/vendor/jquery/jquery.js',
            'admin/js/vendor/select2/select2.full.js',
            'admin/js/vendor/select2/i18n/tr.js',
            'admin/js/jquery.init.js',
            'admin/js/autocomplete.js',
            'djaa_list_filter/admin/js/autocomplete_list_filter.js',
        ]
        css = {
            'screen': [
                'admin/css/vendor/select2/select2.css',
                'admin/css/autocomplete.css',
                'djaa_list_filter/admin/css/autocomplete_list_filter.css',
            ]
        }
