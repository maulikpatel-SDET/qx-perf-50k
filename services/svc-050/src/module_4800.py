"""Service module 4800: business logic, no crypto."""


def calculate_total_4800(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4800():
    return 'module 4800 handles orders and invoices'
