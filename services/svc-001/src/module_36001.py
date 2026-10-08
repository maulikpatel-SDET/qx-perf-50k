"""Service module 36001: business logic, no crypto."""


def calculate_total_36001(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36001():
    return 'module 36001 handles orders and invoices'
