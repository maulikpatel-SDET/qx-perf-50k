"""Service module 2445: business logic, no crypto."""


def calculate_total_2445(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2445():
    return 'module 2445 handles orders and invoices'
