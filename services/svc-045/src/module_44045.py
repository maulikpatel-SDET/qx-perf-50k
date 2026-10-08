"""Service module 44045: business logic, no crypto."""


def calculate_total_44045(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44045():
    return 'module 44045 handles orders and invoices'
