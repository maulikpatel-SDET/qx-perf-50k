"""Service module 43406: business logic, no crypto."""


def calculate_total_43406(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43406():
    return 'module 43406 handles orders and invoices'
