"""Service module 31523: business logic, no crypto."""


def calculate_total_31523(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31523():
    return 'module 31523 handles orders and invoices'
