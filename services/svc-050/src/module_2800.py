"""Service module 2800: business logic, no crypto."""


def calculate_total_2800(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2800():
    return 'module 2800 handles orders and invoices'
