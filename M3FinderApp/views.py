import json
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView
from django.http import JsonResponse
from .models import BusStop, BusStopDestination, Destination, DestinationSubmission
from .forms import DestinationSubmissionForm


# Create your views here.
# def home_screen(request):
#     print (request.headers)
#     return render(request,'base.html', {})
# views.py

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['destinations'] = Destination.objects.all()
        context['bus_stops'] = BusStop.objects.all()

        return context

class EnterDestinationView(TemplateView):
    template_name = 'enter_destination.html'

class TransportationLocationView(TemplateView):
    template_name = 'transportation_location.html'

    def get(self, request, *args, **kwargs):
        destination_name = request.GET.get('destination')
        destination = get_object_or_404(Destination, name=destination_name)
        
        bus_stop_destinations = BusStopDestination.objects.filter(destination=destination)
        bus_stops = [
            {
                'name': bsd.bus_stop.name,
                'latitude': bsd.bus_stop.latitude,
                'longitude': bsd.bus_stop.longitude,
            } for bsd in bus_stop_destinations
        ]

        context = {
            'destination': destination.name,
            'bus_stops': json.dumps(bus_stops),  # Serialize bus_stops to JSON
        }
        return self.render_to_response(context)


def search_destinations(request):
    query = request.GET.get('q')
    if query:
        destinations = Destination.objects.filter(name__icontains=query)
        results = [{'name': destination.name} for destination in destinations]
        return JsonResponse(results, safe=False)
    return JsonResponse([], safe=False)



class ContactUsView(TemplateView):
    template_name = 'contact_us.html'

    def get(self, request, *args, **kwargs):
        form = DestinationSubmissionForm()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = DestinationSubmissionForm(request.POST)
        if form.is_valid():
            DestinationSubmission.objects.create(
                name=form.cleaned_data['name'],
                latitude=form.cleaned_data['latitude'],
                longitude=form.cleaned_data['longitude'],
                additional_info=form.cleaned_data.get('additional_info'),
                message=form.cleaned_data.get('message')
            )
            return redirect('success')
        return self.render_to_response({'form': form})
    
class SuccessView(TemplateView):
    template_name = 'success.html'