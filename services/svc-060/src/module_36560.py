"""Service module 36560: business logic, no crypto."""


def calculate_total_36560(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36560():
    return 'module 36560 handles orders and invoices'
