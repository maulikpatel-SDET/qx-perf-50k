"""Service module 4560: business logic, no crypto."""


def calculate_total_4560(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4560():
    return 'module 4560 handles orders and invoices'
