from django.views.generic import TemplateView
from django.forms.models import modelform_factory
from django.shortcuts import render_to_response
from data.models import ContactDetails
from django.template.context import RequestContext

class ContactView(TemplateView):
    template_name = 'contact.html'

    def post(self, *args, **kwargs):
        ContactForm = modelform_factory(ContactDetails)
        form = ContactForm(data=self.request.POST)
        if form.is_valid():
            form.save()
            success = 'Your Message has been submitted successfully'
        else:
            error = form.errors
        return render_to_response(self.template_name, locals(), context_instance = RequestContext(self.request))



