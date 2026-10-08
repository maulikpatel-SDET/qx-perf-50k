"""Service module 12167: business logic, no crypto."""


def calculate_total_12167(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12167():
    return 'module 12167 handles orders and invoices'
