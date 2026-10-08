"""Service module 18559: business logic, no crypto."""


def calculate_total_18559(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18559():
    return 'module 18559 handles orders and invoices'
