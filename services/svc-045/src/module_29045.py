"""Service module 29045: business logic, no crypto."""


def calculate_total_29045(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29045():
    return 'module 29045 handles orders and invoices'
