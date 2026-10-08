"""Service module 31739: business logic, no crypto."""


def calculate_total_31739(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31739():
    return 'module 31739 handles orders and invoices'
