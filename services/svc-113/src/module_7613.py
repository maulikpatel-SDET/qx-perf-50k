"""Service module 7613: business logic, no crypto."""


def calculate_total_7613(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7613():
    return 'module 7613 handles orders and invoices'
