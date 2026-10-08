"""Service module 28516: business logic, no crypto."""


def calculate_total_28516(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28516():
    return 'module 28516 handles orders and invoices'
