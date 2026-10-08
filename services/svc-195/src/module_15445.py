"""Service module 15445: business logic, no crypto."""


def calculate_total_15445(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15445():
    return 'module 15445 handles orders and invoices'
