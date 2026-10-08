"""Service module 23905: business logic, no crypto."""


def calculate_total_23905(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23905():
    return 'module 23905 handles orders and invoices'
