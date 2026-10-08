"""Service module 44851: business logic, no crypto."""


def calculate_total_44851(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44851():
    return 'module 44851 handles orders and invoices'
