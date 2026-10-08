"""Service module 49851: business logic, no crypto."""


def calculate_total_49851(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49851():
    return 'module 49851 handles orders and invoices'
