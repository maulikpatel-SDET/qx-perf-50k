"""Service module 28292: business logic, no crypto."""


def calculate_total_28292(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28292():
    return 'module 28292 handles orders and invoices'
