"""Service module 43682: business logic, no crypto."""


def calculate_total_43682(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43682():
    return 'module 43682 handles orders and invoices'
