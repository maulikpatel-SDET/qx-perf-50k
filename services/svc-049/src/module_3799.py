"""Service module 3799: business logic, no crypto."""


def calculate_total_3799(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3799():
    return 'module 3799 handles orders and invoices'
