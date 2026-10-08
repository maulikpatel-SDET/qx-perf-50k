"""Service module 15018: business logic, no crypto."""


def calculate_total_15018(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15018():
    return 'module 15018 handles orders and invoices'
