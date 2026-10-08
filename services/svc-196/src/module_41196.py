"""Service module 41196: business logic, no crypto."""


def calculate_total_41196(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41196():
    return 'module 41196 handles orders and invoices'
