"""Service module 1385: business logic, no crypto."""


def calculate_total_1385(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1385():
    return 'module 1385 handles orders and invoices'
