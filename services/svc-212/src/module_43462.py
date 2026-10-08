"""Service module 43462: business logic, no crypto."""


def calculate_total_43462(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43462():
    return 'module 43462 handles orders and invoices'
