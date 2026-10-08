"""Service module 41758: business logic, no crypto."""


def calculate_total_41758(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41758():
    return 'module 41758 handles orders and invoices'
