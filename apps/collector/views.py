from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from apps.users.models import User

from . import forms, models


class ListPlacesView(LoginRequiredMixin, generic.ListView):
    """View for list of places."""

    template_name = "collector/list_places.html"
    context_object_name = "places"

    def get_queryset(self):
        return User.objects.get(id=self.request.user.id).places.all()


class AddPlaceView(LoginRequiredMixin, generic.CreateView):
    """View for Place create."""

    template_name = "collector/add_places.html"
    queryset = models.Place.objects.all()
    model = models.Place
    form_class = forms.PlaceForm

    def check_cookies(self, request):
        """Check cookie and their values."""
        return all(
            [
                "latitude" in request.COOKIES,
                "longitude" in request.COOKIES,
            ]
        )

    def get_success_url(self) -> str:
        """Get url for reverse after success create."""
        return reverse_lazy("collector:list-places")

    def post(self, request, *args, **kwargs):
        """Handler for POST request."""
        self.object = None
        form = self.get_form()
        if all([form.is_valid(), self.check_cookies(request)]):
            return self.form_valid(
                form,
                request,
            )
        return self.form_invalid(form)

    def form_valid(self, form, request):
        """Overridden for save form after create."""
        self.object = form.save(commit=False)
        self.object.latitude = request.COOKIES["latitude"]
        self.object.longitude = request.COOKIES["longitude"]
        self.object.user = request.user
        self.object.save()
        return redirect(self.get_success_url())


class DetailPlaceView(PermissionRequiredMixin, generic.DetailView):
    """View for detail information about place."""

    queryset = models.Place.objects.all()
    template_name = "collector/detail_place.html"
    context_object_name = "place"

    def has_permission(self) -> bool:
        return all(
            [
                self.request.user.id == self.get_object().user.id,
            ]
        )


class DeletePlaceView(PermissionRequiredMixin, generic.DeleteView):
    """View for delete place."""

    model = models.Place

    def get_success_url(self) -> str:
        """Get url for reverse after delete place."""
        return reverse_lazy("collector:list-places")

    def has_permission(self) -> bool:
        return all(
            [
                self.request.user.id == self.get_object().user.id,
            ]
        )


class UpdatePlaceView(PermissionRequiredMixin, generic.UpdateView):
    """View for update place."""

    template_name = "collector/update_place.html"
    form_class = forms.PlaceForm
    queryset = models.Place.objects.all()
    context_object_name = "place"

    def get_success_url(self) -> str:
        """Get url for reverse after delete place."""
        return reverse_lazy(
            "collector:detail-place",
            kwargs={"pk": self.get_object().pk},
        )

    def get_object(self):
        """Get object those will be update."""
        return self.queryset.get(id=self.kwargs["pk"])

    def post(self, request, *args, **kwargs):
        """Handler for POST request."""
        form = forms.PlaceForm(
            request.POST,
            instance=self.get_object(),
        )
        if form.is_valid():
            return self.form_valid(
                form,
                request,
            )
        return self.form_invalid(form)

    def form_valid(self, form, request):
        """Overridden for save form after update."""
        object = form.save(commit=False)
        object.latitude = request.COOKIES["latitude"]
        object.longitude = request.COOKIES["longitude"]
        object.user = request.user
        object.save()
        return redirect(self.get_success_url())

    def has_permission(self) -> bool:
        return all(
            [
                self.request.user.id == self.get_object().user.id,
            ]
        )
