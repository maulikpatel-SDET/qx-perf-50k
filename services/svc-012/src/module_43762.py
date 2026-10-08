"""Service module 43762: business logic, no crypto."""


def calculate_total_43762(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43762():
    return 'module 43762 handles orders and invoices'
