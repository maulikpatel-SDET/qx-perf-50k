"""Service module 43955: business logic, no crypto."""


def calculate_total_43955(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43955():
    return 'module 43955 handles orders and invoices'
