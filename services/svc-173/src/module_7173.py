"""Service module 7173: business logic, no crypto."""


def calculate_total_7173(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7173():
    return 'module 7173 handles orders and invoices'
