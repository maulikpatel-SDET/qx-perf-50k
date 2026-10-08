"""Service module 17051: business logic, no crypto."""


def calculate_total_17051(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17051():
    return 'module 17051 handles orders and invoices'
