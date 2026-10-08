"""Service module 4049: business logic, no crypto."""


def calculate_total_4049(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4049():
    return 'module 4049 handles orders and invoices'
