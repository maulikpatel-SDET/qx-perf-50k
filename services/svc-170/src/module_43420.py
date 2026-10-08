"""Service module 43420: business logic, no crypto."""


def calculate_total_43420(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43420():
    return 'module 43420 handles orders and invoices'
