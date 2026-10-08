"""Service module 48074: business logic, no crypto."""


def calculate_total_48074(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48074():
    return 'module 48074 handles orders and invoices'
