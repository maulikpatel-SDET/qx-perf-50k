"""Service module 14851: business logic, no crypto."""


def calculate_total_14851(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14851():
    return 'module 14851 handles orders and invoices'
