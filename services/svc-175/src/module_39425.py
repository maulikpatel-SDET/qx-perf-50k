"""Service module 39425: business logic, no crypto."""


def calculate_total_39425(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39425():
    return 'module 39425 handles orders and invoices'
