"""Service module 39619: business logic, no crypto."""


def calculate_total_39619(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39619():
    return 'module 39619 handles orders and invoices'
