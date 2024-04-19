#==================================================> Imports <==================================================
# ----> genrel imports <----
from django import forms


# ----> extrenal imports <----
from .models import *




#===============================================> ReasonBack Form <===============================================

class ReasonBackForm(forms.ModelForm):
    class Meta:
        model =ReasonBack
        fields = '__all__'




#================================================> Courier Form <=================================================

class CourierForm(forms.ModelForm):
    class Meta:
        model = Courier
        fields = '__all__'


#================================================> ReportCourier Form <=================================================

class ReportCourierForm(forms.ModelForm):
    class Meta :
        model = ReportCuorier
        fields = '__all__'
        widgets= {
            'user': forms.Select(attrs={'class': 'form-control',
                                                'style': 'font-size: 14px;'}),
            'courier': forms.Select(attrs={'class': 'form-control',
                                                'style': 'font-size: 14px;'}),
            'reason_back': forms.Select(attrs={'class': 'form-control',
                                                'style': 'font-size: 14px;'}),
            'duty_to_pay1': forms.Select(attrs={'class': 'form-control',
                                                'style': 'font-size: 14px;'}),
            'duty_to_pay2': forms.Select(attrs={'class': 'form-control',
                                                'style': 'font-size: 14px;'}),
            'target_number': forms.Select(attrs={'class': 'form-control',
                                                'style': 'font-size: 14px;'}),
            'cost_courier1': forms.TextInput(attrs={'class': 'form-control',
                                                'style': 'font-size: 14px;'}),
            'cost_courier2': forms.TextInput(attrs={'class': 'form-control',
                                                'style': 'font-size: 14px;'}),


        }