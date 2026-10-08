"""Service module 21940: business logic, no crypto."""


def calculate_total_21940(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21940():
    return 'module 21940 handles orders and invoices'
