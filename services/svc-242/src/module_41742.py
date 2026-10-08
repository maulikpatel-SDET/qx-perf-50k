"""Service module 41742: business logic, no crypto."""


def calculate_total_41742(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41742():
    return 'module 41742 handles orders and invoices'
