"""Service module 43458: business logic, no crypto."""


def calculate_total_43458(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43458():
    return 'module 43458 handles orders and invoices'
