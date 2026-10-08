"""Service module 13385: business logic, no crypto."""


def calculate_total_13385(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13385():
    return 'module 13385 handles orders and invoices'
