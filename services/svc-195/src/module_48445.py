"""Service module 48445: business logic, no crypto."""


def calculate_total_48445(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48445():
    return 'module 48445 handles orders and invoices'
