"""Service module 3018: business logic, no crypto."""


def calculate_total_3018(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3018():
    return 'module 3018 handles orders and invoices'
