"""Service module 43397: business logic, no crypto."""


def calculate_total_43397(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43397():
    return 'module 43397 handles orders and invoices'
