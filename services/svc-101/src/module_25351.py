"""Service module 25351: business logic, no crypto."""


def calculate_total_25351(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25351():
    return 'module 25351 handles orders and invoices'
