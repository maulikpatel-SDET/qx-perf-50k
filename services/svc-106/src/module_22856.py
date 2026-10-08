"""Service module 22856: business logic, no crypto."""


def calculate_total_22856(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22856():
    return 'module 22856 handles orders and invoices'
