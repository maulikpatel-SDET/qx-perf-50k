"""Service module 2360: business logic, no crypto."""


def calculate_total_2360(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2360():
    return 'module 2360 handles orders and invoices'
