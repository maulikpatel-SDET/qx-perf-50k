"""Service module 15851: business logic, no crypto."""


def calculate_total_15851(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15851():
    return 'module 15851 handles orders and invoices'
