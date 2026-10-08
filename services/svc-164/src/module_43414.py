"""Service module 43414: business logic, no crypto."""


def calculate_total_43414(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43414():
    return 'module 43414 handles orders and invoices'
