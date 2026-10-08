"""Service module 45762: business logic, no crypto."""


def calculate_total_45762(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45762():
    return 'module 45762 handles orders and invoices'
