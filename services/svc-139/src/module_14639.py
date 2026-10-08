"""Service module 14639: business logic, no crypto."""


def calculate_total_14639(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14639():
    return 'module 14639 handles orders and invoices'
