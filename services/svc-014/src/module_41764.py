"""Service module 41764: business logic, no crypto."""


def calculate_total_41764(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41764():
    return 'module 41764 handles orders and invoices'
