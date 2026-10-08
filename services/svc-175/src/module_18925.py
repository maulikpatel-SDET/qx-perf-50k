"""Service module 18925: business logic, no crypto."""


def calculate_total_18925(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18925():
    return 'module 18925 handles orders and invoices'
