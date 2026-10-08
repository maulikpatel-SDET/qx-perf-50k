"""Service module 8739: business logic, no crypto."""


def calculate_total_8739(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8739():
    return 'module 8739 handles orders and invoices'
