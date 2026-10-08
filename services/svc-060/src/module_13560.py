"""Service module 13560: business logic, no crypto."""


def calculate_total_13560(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13560():
    return 'module 13560 handles orders and invoices'
