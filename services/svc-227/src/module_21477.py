"""Service module 21477: business logic, no crypto."""


def calculate_total_21477(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21477():
    return 'module 21477 handles orders and invoices'
