"""Service module 46486: business logic, no crypto."""


def calculate_total_46486(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46486():
    return 'module 46486 handles orders and invoices'
