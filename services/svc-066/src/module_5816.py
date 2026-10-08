"""Service module 5816: business logic, no crypto."""


def calculate_total_5816(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5816():
    return 'module 5816 handles orders and invoices'
