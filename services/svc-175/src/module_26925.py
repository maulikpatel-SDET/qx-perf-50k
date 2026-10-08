"""Service module 26925: business logic, no crypto."""


def calculate_total_26925(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26925():
    return 'module 26925 handles orders and invoices'
