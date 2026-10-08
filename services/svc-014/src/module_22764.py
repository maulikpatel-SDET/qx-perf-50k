"""Service module 22764: business logic, no crypto."""


def calculate_total_22764(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22764():
    return 'module 22764 handles orders and invoices'
