"""Service module 21156: business logic, no crypto."""


def calculate_total_21156(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21156():
    return 'module 21156 handles orders and invoices'
