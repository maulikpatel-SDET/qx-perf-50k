"""Service module 46045: business logic, no crypto."""


def calculate_total_46045(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46045():
    return 'module 46045 handles orders and invoices'
