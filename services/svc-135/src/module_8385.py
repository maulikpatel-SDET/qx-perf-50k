"""Service module 8385: business logic, no crypto."""


def calculate_total_8385(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8385():
    return 'module 8385 handles orders and invoices'
