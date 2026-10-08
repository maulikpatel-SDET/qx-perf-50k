"""Service module 43250: business logic, no crypto."""


def calculate_total_43250(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43250():
    return 'module 43250 handles orders and invoices'
