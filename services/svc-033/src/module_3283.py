"""Service module 3283: business logic, no crypto."""


def calculate_total_3283(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3283():
    return 'module 3283 handles orders and invoices'
