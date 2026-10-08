"""Service module 41925: business logic, no crypto."""


def calculate_total_41925(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41925():
    return 'module 41925 handles orders and invoices'
