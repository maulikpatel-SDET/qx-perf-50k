"""Service module 48977: business logic, no crypto."""


def calculate_total_48977(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48977():
    return 'module 48977 handles orders and invoices'
