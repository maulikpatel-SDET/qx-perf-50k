"""Service module 28959: business logic, no crypto."""


def calculate_total_28959(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28959():
    return 'module 28959 handles orders and invoices'
