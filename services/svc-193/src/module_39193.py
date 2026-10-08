"""Service module 39193: business logic, no crypto."""


def calculate_total_39193(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39193():
    return 'module 39193 handles orders and invoices'
