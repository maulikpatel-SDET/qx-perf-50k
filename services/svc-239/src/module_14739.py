"""Service module 14739: business logic, no crypto."""


def calculate_total_14739(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14739():
    return 'module 14739 handles orders and invoices'
