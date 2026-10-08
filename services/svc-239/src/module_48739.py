"""Service module 48739: business logic, no crypto."""


def calculate_total_48739(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48739():
    return 'module 48739 handles orders and invoices'
