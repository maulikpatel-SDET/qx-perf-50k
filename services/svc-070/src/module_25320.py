"""Service module 25320: business logic, no crypto."""


def calculate_total_25320(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25320():
    return 'module 25320 handles orders and invoices'
