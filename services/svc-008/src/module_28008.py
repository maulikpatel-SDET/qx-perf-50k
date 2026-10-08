"""Service module 28008: business logic, no crypto."""


def calculate_total_28008(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28008():
    return 'module 28008 handles orders and invoices'
