"""Service module 19385: business logic, no crypto."""


def calculate_total_19385(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19385():
    return 'module 19385 handles orders and invoices'
