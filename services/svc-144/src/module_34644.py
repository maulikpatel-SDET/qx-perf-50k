"""Service module 34644: business logic, no crypto."""


def calculate_total_34644(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34644():
    return 'module 34644 handles orders and invoices'
