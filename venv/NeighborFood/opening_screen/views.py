from django.views.generic.edit import FormView

from . import forms

class Index(FormView):
    form_class = forms.TextForm
    template_name = "opening_screen/index.html"

    def form_valid(self, form):
        data = form.cleaned_data
        text = data["text"]

        ctxt = self.get_context_data(text=text, form=form)
        return self.render_to_response(ctxt)
