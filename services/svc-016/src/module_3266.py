"""Service module 3266: business logic, no crypto."""


def calculate_total_3266(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3266():
    return 'module 3266 handles orders and invoices'
