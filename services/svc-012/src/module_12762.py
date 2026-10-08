"""Service module 12762: business logic, no crypto."""


def calculate_total_12762(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12762():
    return 'module 12762 handles orders and invoices'
