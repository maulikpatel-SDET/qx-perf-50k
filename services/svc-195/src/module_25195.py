"""Service module 25195: business logic, no crypto."""


def calculate_total_25195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25195():
    return 'module 25195 handles orders and invoices'
