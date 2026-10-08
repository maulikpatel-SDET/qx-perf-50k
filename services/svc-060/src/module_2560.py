"""Service module 2560: business logic, no crypto."""


def calculate_total_2560(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2560():
    return 'module 2560 handles orders and invoices'
