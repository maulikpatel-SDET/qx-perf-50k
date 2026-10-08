"""Service module 6385: business logic, no crypto."""


def calculate_total_6385(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6385():
    return 'module 6385 handles orders and invoices'
