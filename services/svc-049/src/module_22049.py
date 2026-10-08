"""Service module 22049: business logic, no crypto."""


def calculate_total_22049(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22049():
    return 'module 22049 handles orders and invoices'
