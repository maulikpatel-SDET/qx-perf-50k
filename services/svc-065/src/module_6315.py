"""Service module 6315: business logic, no crypto."""


def calculate_total_6315(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6315():
    return 'module 6315 handles orders and invoices'
