"""Service module 37410: business logic, no crypto."""


def calculate_total_37410(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37410():
    return 'module 37410 handles orders and invoices'
