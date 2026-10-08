"""Service module 37762: business logic, no crypto."""


def calculate_total_37762(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37762():
    return 'module 37762 handles orders and invoices'
