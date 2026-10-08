"""Service module 3812: business logic, no crypto."""


def calculate_total_3812(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3812():
    return 'module 3812 handles orders and invoices'
