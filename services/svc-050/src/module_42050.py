"""Service module 42050: business logic, no crypto."""


def calculate_total_42050(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42050():
    return 'module 42050 handles orders and invoices'
