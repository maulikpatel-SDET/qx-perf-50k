"""Service module 43542: business logic, no crypto."""


def calculate_total_43542(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43542():
    return 'module 43542 handles orders and invoices'
