"""Service module 47925: business logic, no crypto."""


def calculate_total_47925(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47925():
    return 'module 47925 handles orders and invoices'
