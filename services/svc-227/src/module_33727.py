"""Service module 33727: business logic, no crypto."""


def calculate_total_33727(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33727():
    return 'module 33727 handles orders and invoices'
