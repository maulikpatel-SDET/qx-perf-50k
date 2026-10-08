"""Service module 12639: business logic, no crypto."""


def calculate_total_12639(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12639():
    return 'module 12639 handles orders and invoices'
