"""Service module 43674: business logic, no crypto."""


def calculate_total_43674(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43674():
    return 'module 43674 handles orders and invoices'
