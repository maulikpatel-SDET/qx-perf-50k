"""Service module 2925: business logic, no crypto."""


def calculate_total_2925(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2925():
    return 'module 2925 handles orders and invoices'
