"""Service module 47196: business logic, no crypto."""


def calculate_total_47196(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47196():
    return 'module 47196 handles orders and invoices'
