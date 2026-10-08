"""Service module 29025: business logic, no crypto."""


def calculate_total_29025(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29025():
    return 'module 29025 handles orders and invoices'
