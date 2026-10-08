"""Service module 43543: business logic, no crypto."""


def calculate_total_43543(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43543():
    return 'module 43543 handles orders and invoices'
