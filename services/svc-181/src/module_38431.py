"""Service module 38431: business logic, no crypto."""


def calculate_total_38431(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38431():
    return 'module 38431 handles orders and invoices'
