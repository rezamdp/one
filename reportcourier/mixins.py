class CreateReportCourierMixin():

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['user', 'reason_back', 'courier', 'name_customer', 'target_number', 'target1', 'target2',
                           'duty_to_pay1', 'duty_to_pay2',
                           'back_courier1', 'back_courier2', 'cost_courier1', 'cost_courier2', 'number_bigak1',
                           'number_bigak2']
        else:
            self.fields = ['reason_back', 'courier', 'name_customer', 'target_number', 'target1', 'target2',
                           'duty_to_pay1', 'duty_to_pay2',
                           'back_courier1', 'back_courier2', 'cost_courier1', 'cost_courier2', 'number_bigak1',
                           'number_bigak2']

        return super().dispatch(request, *args, **kwargs)

