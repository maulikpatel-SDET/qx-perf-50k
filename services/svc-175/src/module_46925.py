"""Service module 46925: business logic, no crypto."""


def calculate_total_46925(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46925():
    return 'module 46925 handles orders and invoices'
