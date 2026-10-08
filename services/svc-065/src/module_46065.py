"""Service module 46065: business logic, no crypto."""


def calculate_total_46065(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46065():
    return 'module 46065 handles orders and invoices'
