"""Service module 21425: business logic, no crypto."""


def calculate_total_21425(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21425():
    return 'module 21425 handles orders and invoices'
