from django.urls import reverse, resolve


def test_values_list():
    path = reverse('values_list')
    assert resolve(path).view_name == 'values_list'


def test_value_detail():
    path = reverse('value_detail', kwargs={'pk': 2})
    assert resolve(path).view_name == 'value_detail'


def test_principles_list():
    path = reverse('principles_list')
    assert resolve(path).view_name == 'principles_list'


def test_principle_detail():
    path = reverse('principle_detail', kwargs={'pk': 2})
    assert resolve(path).view_name == 'principle_detail'
