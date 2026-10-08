"""Service module 43972: business logic, no crypto."""


def calculate_total_43972(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43972():
    return 'module 43972 handles orders and invoices'
