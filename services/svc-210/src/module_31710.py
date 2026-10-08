"""Service module 31710: business logic, no crypto."""


def calculate_total_31710(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31710():
    return 'module 31710 handles orders and invoices'
