"""Service module 35375: business logic, no crypto."""


def calculate_total_35375(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35375():
    return 'module 35375 handles orders and invoices'
