"""Service module 26368: business logic, no crypto."""


def calculate_total_26368(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26368():
    return 'module 26368 handles orders and invoices'
