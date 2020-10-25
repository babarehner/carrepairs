from django import forms
from django.forms import \
    ValidationError
from carrepairs.models import \
    Vehicles

class VehiclesForm(forms.ModelForm):

    class Meta:
        # Additional info to help Django provide intelligent defaults
        model = Vehicles
        fields = ['id', 'year', 'manufacturer', 'model', 'serial_no']

    @staticmethod
    def validate_vehicle_fields( year: int,
                                manufacturer: str,
                                model: str,
                                serial_no: str,):

        if year > 1910 and year < 2030:
            ...
        else:
            raise ValidationError( 'Car year must be between 1910 and 2030')

        if len(manufacturer) > Vehicles.manufacturer.max_length:
            raise ValidationError('The manufacturers name must be less than ' +
                                  Vehicles.manufacturer.max_length +
                                  'characters.')

        if len(model) > Vehicles.model_max_length:
            raise ValidationError('The manufacturers name must be less than ' +
                                  Vehicles.model.max_length +
                                  ' characters.')

        if len(serial_no) > Vehicles.serial_no.max_length:
            raise ValidationError(' The serial number must be less than ' +
                                  Vehicles.serial_no.max_length +
                                  ' characters.')
        # Need to verify that this works
        if serial_no in Vehicles.objects.filter(serial_no='serial_no'):
            raise ValidationError('There already is a vehicle in the database'
                                  ' with that same serial number.')
        return

    def clean(self):
        # Clean and validate the data
        cleaned_data = super().clean()
        year = cleaned_data.get('year')
        manufacturer = cleaned_data.get('manufacturer')
        model = cleaned_data.get('model')
        serial_no = cleaned_data.get('serial_no')
        self.validate_vehicle_fields(year, manufacturer, model, serial_no)
        return

