"""Service module 43006: business logic, no crypto."""


def calculate_total_43006(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43006():
    return 'module 43006 handles orders and invoices'
