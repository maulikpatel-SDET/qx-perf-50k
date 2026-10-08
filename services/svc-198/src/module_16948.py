"""Service module 16948: business logic, no crypto."""


def calculate_total_16948(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16948():
    return 'module 16948 handles orders and invoices'
