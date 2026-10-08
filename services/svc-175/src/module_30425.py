"""Service module 30425: business logic, no crypto."""


def calculate_total_30425(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30425():
    return 'module 30425 handles orders and invoices'
