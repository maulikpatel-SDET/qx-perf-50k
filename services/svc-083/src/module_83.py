"""Service module 83: business logic, no crypto."""


def calculate_total_83(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_83():
    return 'module 83 handles orders and invoices'
