"""Service module 39725: business logic, no crypto."""


def calculate_total_39725(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39725():
    return 'module 39725 handles orders and invoices'
