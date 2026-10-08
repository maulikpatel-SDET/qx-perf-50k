"""Service module 36425: business logic, no crypto."""


def calculate_total_36425(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36425():
    return 'module 36425 handles orders and invoices'
