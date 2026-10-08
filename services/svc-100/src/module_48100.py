"""Service module 48100: business logic, no crypto."""


def calculate_total_48100(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48100():
    return 'module 48100 handles orders and invoices'
