"""Service module 1925: business logic, no crypto."""


def calculate_total_1925(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1925():
    return 'module 1925 handles orders and invoices'
