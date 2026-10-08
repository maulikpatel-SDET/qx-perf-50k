"""Service module 17049: business logic, no crypto."""


def calculate_total_17049(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17049():
    return 'module 17049 handles orders and invoices'
