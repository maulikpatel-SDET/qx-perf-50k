"""Service module 18560: business logic, no crypto."""


def calculate_total_18560(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18560():
    return 'module 18560 handles orders and invoices'
