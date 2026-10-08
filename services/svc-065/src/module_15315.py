"""Service module 15315: business logic, no crypto."""


def calculate_total_15315(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15315():
    return 'module 15315 handles orders and invoices'
