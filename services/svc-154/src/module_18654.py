"""Service module 18654: business logic, no crypto."""


def calculate_total_18654(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18654():
    return 'module 18654 handles orders and invoices'
