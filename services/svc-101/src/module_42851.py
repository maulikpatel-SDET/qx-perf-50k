"""Service module 42851: business logic, no crypto."""


def calculate_total_42851(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42851():
    return 'module 42851 handles orders and invoices'
