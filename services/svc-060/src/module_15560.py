"""Service module 15560: business logic, no crypto."""


def calculate_total_15560(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15560():
    return 'module 15560 handles orders and invoices'
