"""Service module 29739: business logic, no crypto."""


def calculate_total_29739(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29739():
    return 'module 29739 handles orders and invoices'
