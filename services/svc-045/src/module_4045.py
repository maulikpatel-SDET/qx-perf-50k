"""Service module 4045: business logic, no crypto."""


def calculate_total_4045(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4045():
    return 'module 4045 handles orders and invoices'
