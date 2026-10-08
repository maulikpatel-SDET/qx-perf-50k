"""Service module 35825: business logic, no crypto."""


def calculate_total_35825(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35825():
    return 'module 35825 handles orders and invoices'
