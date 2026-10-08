"""Service module 43013: business logic, no crypto."""


def calculate_total_43013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43013():
    return 'module 43013 handles orders and invoices'
