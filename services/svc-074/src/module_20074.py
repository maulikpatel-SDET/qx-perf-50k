"""Service module 20074: business logic, no crypto."""


def calculate_total_20074(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20074():
    return 'module 20074 handles orders and invoices'
