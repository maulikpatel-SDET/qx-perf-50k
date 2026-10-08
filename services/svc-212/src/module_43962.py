"""Service module 43962: business logic, no crypto."""


def calculate_total_43962(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43962():
    return 'module 43962 handles orders and invoices'
