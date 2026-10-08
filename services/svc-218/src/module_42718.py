"""Service module 42718: business logic, no crypto."""


def calculate_total_42718(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42718():
    return 'module 42718 handles orders and invoices'
