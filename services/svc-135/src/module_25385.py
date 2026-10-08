"""Service module 25385: business logic, no crypto."""


def calculate_total_25385(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25385():
    return 'module 25385 handles orders and invoices'
