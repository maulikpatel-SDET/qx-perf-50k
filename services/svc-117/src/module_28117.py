"""Service module 28117: business logic, no crypto."""


def calculate_total_28117(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28117():
    return 'module 28117 handles orders and invoices'
