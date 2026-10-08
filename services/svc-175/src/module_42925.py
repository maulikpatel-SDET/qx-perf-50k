"""Service module 42925: business logic, no crypto."""


def calculate_total_42925(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42925():
    return 'module 42925 handles orders and invoices'
