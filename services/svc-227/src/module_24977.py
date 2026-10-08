"""Service module 24977: business logic, no crypto."""


def calculate_total_24977(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24977():
    return 'module 24977 handles orders and invoices'
