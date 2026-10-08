"""Service module 43721: business logic, no crypto."""


def calculate_total_43721(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43721():
    return 'module 43721 handles orders and invoices'
