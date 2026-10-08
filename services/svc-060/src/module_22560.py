"""Service module 22560: business logic, no crypto."""


def calculate_total_22560(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22560():
    return 'module 22560 handles orders and invoices'
