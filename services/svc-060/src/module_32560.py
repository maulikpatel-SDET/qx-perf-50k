"""Service module 32560: business logic, no crypto."""


def calculate_total_32560(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32560():
    return 'module 32560 handles orders and invoices'
