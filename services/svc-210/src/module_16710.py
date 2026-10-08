"""Service module 16710: business logic, no crypto."""


def calculate_total_16710(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16710():
    return 'module 16710 handles orders and invoices'
