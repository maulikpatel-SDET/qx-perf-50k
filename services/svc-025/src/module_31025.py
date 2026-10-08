"""Service module 31025: business logic, no crypto."""


def calculate_total_31025(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31025():
    return 'module 31025 handles orders and invoices'
