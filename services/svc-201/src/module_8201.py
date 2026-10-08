"""Service module 8201: business logic, no crypto."""


def calculate_total_8201(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8201():
    return 'module 8201 handles orders and invoices'
