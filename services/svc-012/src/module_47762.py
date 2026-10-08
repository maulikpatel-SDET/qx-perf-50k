"""Service module 47762: business logic, no crypto."""


def calculate_total_47762(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47762():
    return 'module 47762 handles orders and invoices'
