"""Service module 41156: business logic, no crypto."""


def calculate_total_41156(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41156():
    return 'module 41156 handles orders and invoices'
