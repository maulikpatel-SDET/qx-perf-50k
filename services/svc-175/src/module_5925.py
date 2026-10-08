"""Service module 5925: business logic, no crypto."""


def calculate_total_5925(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5925():
    return 'module 5925 handles orders and invoices'
