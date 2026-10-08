"""Service module 18284: business logic, no crypto."""


def calculate_total_18284(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18284():
    return 'module 18284 handles orders and invoices'
