"""Service module 6977: business logic, no crypto."""


def calculate_total_6977(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6977():
    return 'module 6977 handles orders and invoices'
