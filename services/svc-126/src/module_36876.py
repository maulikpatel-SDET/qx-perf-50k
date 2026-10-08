"""Service module 36876: business logic, no crypto."""


def calculate_total_36876(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36876():
    return 'module 36876 handles orders and invoices'
