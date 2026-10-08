"""Service module 43352: business logic, no crypto."""


def calculate_total_43352(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43352():
    return 'module 43352 handles orders and invoices'
