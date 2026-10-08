"""Service module 26196: business logic, no crypto."""


def calculate_total_26196(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26196():
    return 'module 26196 handles orders and invoices'
