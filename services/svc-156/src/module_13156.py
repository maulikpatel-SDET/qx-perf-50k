"""Service module 13156: business logic, no crypto."""


def calculate_total_13156(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13156():
    return 'module 13156 handles orders and invoices'
