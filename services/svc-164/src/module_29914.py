"""Service module 29914: business logic, no crypto."""


def calculate_total_29914(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29914():
    return 'module 29914 handles orders and invoices'
