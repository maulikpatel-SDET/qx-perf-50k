"""Service module 17789: business logic, no crypto."""


def calculate_total_17789(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17789():
    return 'module 17789 handles orders and invoices'
