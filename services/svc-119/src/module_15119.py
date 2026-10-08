"""Service module 15119: business logic, no crypto."""


def calculate_total_15119(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15119():
    return 'module 15119 handles orders and invoices'
