"""Service module 16049: business logic, no crypto."""


def calculate_total_16049(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16049():
    return 'module 16049 handles orders and invoices'
