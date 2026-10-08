"""Service module 4739: business logic, no crypto."""


def calculate_total_4739(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4739():
    return 'module 4739 handles orders and invoices'
