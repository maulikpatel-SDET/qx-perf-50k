"""Service module 5560: business logic, no crypto."""


def calculate_total_5560(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5560():
    return 'module 5560 handles orders and invoices'
