"""Service module 14531: business logic, no crypto."""


def calculate_total_14531(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14531():
    return 'module 14531 handles orders and invoices'
