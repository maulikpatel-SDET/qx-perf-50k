"""Service module 35027: business logic, no crypto."""


def calculate_total_35027(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35027():
    return 'module 35027 handles orders and invoices'
