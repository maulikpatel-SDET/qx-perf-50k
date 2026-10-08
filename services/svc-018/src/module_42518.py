"""Service module 42518: business logic, no crypto."""


def calculate_total_42518(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42518():
    return 'module 42518 handles orders and invoices'
