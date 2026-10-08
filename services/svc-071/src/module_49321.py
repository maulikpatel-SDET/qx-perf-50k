"""Service module 49321: business logic, no crypto."""


def calculate_total_49321(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49321():
    return 'module 49321 handles orders and invoices'
