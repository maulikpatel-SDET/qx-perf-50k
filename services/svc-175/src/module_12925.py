"""Service module 12925: business logic, no crypto."""


def calculate_total_12925(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12925():
    return 'module 12925 handles orders and invoices'
