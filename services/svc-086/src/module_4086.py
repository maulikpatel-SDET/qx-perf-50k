"""Service module 4086: business logic, no crypto."""


def calculate_total_4086(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4086():
    return 'module 4086 handles orders and invoices'
