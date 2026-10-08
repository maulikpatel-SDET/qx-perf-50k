"""Service module 43027: business logic, no crypto."""


def calculate_total_43027(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43027():
    return 'module 43027 handles orders and invoices'
