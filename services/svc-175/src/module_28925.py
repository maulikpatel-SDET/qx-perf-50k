"""Service module 28925: business logic, no crypto."""


def calculate_total_28925(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28925():
    return 'module 28925 handles orders and invoices'
