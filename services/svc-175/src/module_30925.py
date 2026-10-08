"""Service module 30925: business logic, no crypto."""


def calculate_total_30925(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30925():
    return 'module 30925 handles orders and invoices'
