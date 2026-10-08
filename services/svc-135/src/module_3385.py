"""Service module 3385: business logic, no crypto."""


def calculate_total_3385(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3385():
    return 'module 3385 handles orders and invoices'
