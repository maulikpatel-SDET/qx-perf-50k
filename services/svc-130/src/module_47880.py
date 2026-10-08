"""Service module 47880: business logic, no crypto."""


def calculate_total_47880(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47880():
    return 'module 47880 handles orders and invoices'
