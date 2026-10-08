"""Service module 28156: business logic, no crypto."""


def calculate_total_28156(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28156():
    return 'module 28156 handles orders and invoices'
