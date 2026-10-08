"""Service module 34661: business logic, no crypto."""


def calculate_total_34661(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34661():
    return 'module 34661 handles orders and invoices'
