"""Service module 43211: business logic, no crypto."""


def calculate_total_43211(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43211():
    return 'module 43211 handles orders and invoices'
