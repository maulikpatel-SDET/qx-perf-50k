"""Service module 43237: business logic, no crypto."""


def calculate_total_43237(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43237():
    return 'module 43237 handles orders and invoices'
