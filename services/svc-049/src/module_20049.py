"""Service module 20049: business logic, no crypto."""


def calculate_total_20049(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20049():
    return 'module 20049 handles orders and invoices'
