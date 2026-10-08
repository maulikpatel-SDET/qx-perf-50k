"""Service module 37045: business logic, no crypto."""


def calculate_total_37045(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37045():
    return 'module 37045 handles orders and invoices'
