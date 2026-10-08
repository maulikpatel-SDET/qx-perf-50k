"""Service module 36173: business logic, no crypto."""


def calculate_total_36173(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36173():
    return 'module 36173 handles orders and invoices'
