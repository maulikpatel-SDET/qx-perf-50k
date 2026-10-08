"""Service module 28604: business logic, no crypto."""


def calculate_total_28604(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28604():
    return 'module 28604 handles orders and invoices'
