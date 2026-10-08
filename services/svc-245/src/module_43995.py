"""Service module 43995: business logic, no crypto."""


def calculate_total_43995(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43995():
    return 'module 43995 handles orders and invoices'
