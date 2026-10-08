"""Service module 12494: business logic, no crypto."""


def calculate_total_12494(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12494():
    return 'module 12494 handles orders and invoices'
