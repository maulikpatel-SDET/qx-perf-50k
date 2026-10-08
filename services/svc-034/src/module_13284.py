"""Service module 13284: business logic, no crypto."""


def calculate_total_13284(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13284():
    return 'module 13284 handles orders and invoices'
