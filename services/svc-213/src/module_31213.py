"""Service module 31213: business logic, no crypto."""


def calculate_total_31213(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31213():
    return 'module 31213 handles orders and invoices'
