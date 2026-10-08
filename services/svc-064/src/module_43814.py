"""Service module 43814: business logic, no crypto."""


def calculate_total_43814(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43814():
    return 'module 43814 handles orders and invoices'
