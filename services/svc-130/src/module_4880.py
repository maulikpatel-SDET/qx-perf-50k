"""Service module 4880: business logic, no crypto."""


def calculate_total_4880(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4880():
    return 'module 4880 handles orders and invoices'
