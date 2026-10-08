"""Service module 49800: business logic, no crypto."""


def calculate_total_49800(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49800():
    return 'module 49800 handles orders and invoices'
