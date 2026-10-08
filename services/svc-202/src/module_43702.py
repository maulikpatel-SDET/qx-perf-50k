"""Service module 43702: business logic, no crypto."""


def calculate_total_43702(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43702():
    return 'module 43702 handles orders and invoices'
