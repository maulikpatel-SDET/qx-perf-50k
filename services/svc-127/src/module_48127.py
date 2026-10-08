"""Service module 48127: business logic, no crypto."""


def calculate_total_48127(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48127():
    return 'module 48127 handles orders and invoices'
