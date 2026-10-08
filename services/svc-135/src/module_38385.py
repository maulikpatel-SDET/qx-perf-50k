"""Service module 38385: business logic, no crypto."""


def calculate_total_38385(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38385():
    return 'module 38385 handles orders and invoices'
