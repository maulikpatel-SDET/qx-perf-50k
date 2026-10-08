"""Service module 26625: business logic, no crypto."""


def calculate_total_26625(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26625():
    return 'module 26625 handles orders and invoices'
