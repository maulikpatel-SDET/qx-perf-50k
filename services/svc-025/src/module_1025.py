"""Service module 1025: business logic, no crypto."""


def calculate_total_1025(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1025():
    return 'module 1025 handles orders and invoices'
