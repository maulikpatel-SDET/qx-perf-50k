"""Service module 48495: business logic, no crypto."""


def calculate_total_48495(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48495():
    return 'module 48495 handles orders and invoices'
