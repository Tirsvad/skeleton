from django.views.generic import TemplateView

class baseview(TemplateView):
    template_name = "home.html"
    project = "{{ project_name }}"
    title = "{{ project_name }}"

    def get_context_data(self, **kwargs):
        context = super(baseview, self).get_context_data(**kwargs)
        context['title'] = self.title
        context['project'] = self.project.capitalize()
        return context

class HomeView(baseview):
    title = baseview.title + ' ' + 'skeleton'

class AboutView(baseview):
    template_name = "home.html"