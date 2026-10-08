"""Service module 8383: business logic, no crypto."""


def calculate_total_8383(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8383():
    return 'module 8383 handles orders and invoices'
