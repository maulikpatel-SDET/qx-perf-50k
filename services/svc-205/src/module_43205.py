"""Service module 43205: business logic, no crypto."""


def calculate_total_43205(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43205():
    return 'module 43205 handles orders and invoices'
