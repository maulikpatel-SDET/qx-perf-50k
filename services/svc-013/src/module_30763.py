"""Service module 30763: business logic, no crypto."""


def calculate_total_30763(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30763():
    return 'module 30763 handles orders and invoices'
