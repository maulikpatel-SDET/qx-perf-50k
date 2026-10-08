"""Service module 43208: business logic, no crypto."""


def calculate_total_43208(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43208():
    return 'module 43208 handles orders and invoices'
