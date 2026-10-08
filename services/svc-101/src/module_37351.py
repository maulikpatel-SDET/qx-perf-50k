"""Service module 37351: business logic, no crypto."""


def calculate_total_37351(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37351():
    return 'module 37351 handles orders and invoices'
