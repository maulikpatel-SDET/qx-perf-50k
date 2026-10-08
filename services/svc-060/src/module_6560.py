"""Service module 6560: business logic, no crypto."""


def calculate_total_6560(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6560():
    return 'module 6560 handles orders and invoices'
