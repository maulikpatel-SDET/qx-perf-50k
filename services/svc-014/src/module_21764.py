"""Service module 21764: business logic, no crypto."""


def calculate_total_21764(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21764():
    return 'module 21764 handles orders and invoices'
