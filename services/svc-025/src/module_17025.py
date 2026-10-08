"""Service module 17025: business logic, no crypto."""


def calculate_total_17025(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17025():
    return 'module 17025 handles orders and invoices'
