"""Service module 10800: business logic, no crypto."""


def calculate_total_10800(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10800():
    return 'module 10800 handles orders and invoices'
