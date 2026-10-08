"""Service module 43991: business logic, no crypto."""


def calculate_total_43991(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43991():
    return 'module 43991 handles orders and invoices'
