"""Service module 43784: business logic, no crypto."""


def calculate_total_43784(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43784():
    return 'module 43784 handles orders and invoices'
