"""Service module 3323: business logic, no crypto."""


def calculate_total_3323(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3323():
    return 'module 3323 handles orders and invoices'
