"""Service module 41495: business logic, no crypto."""


def calculate_total_41495(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41495():
    return 'module 41495 handles orders and invoices'
