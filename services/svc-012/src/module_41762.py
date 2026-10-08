"""Service module 41762: business logic, no crypto."""


def calculate_total_41762(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41762():
    return 'module 41762 handles orders and invoices'
