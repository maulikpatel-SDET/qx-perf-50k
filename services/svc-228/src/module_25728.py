"""Service module 25728: business logic, no crypto."""


def calculate_total_25728(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25728():
    return 'module 25728 handles orders and invoices'
