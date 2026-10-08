"""Service module 44763: business logic, no crypto."""


def calculate_total_44763(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44763():
    return 'module 44763 handles orders and invoices'
