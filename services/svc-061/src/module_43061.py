"""Service module 43061: business logic, no crypto."""


def calculate_total_43061(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43061():
    return 'module 43061 handles orders and invoices'
