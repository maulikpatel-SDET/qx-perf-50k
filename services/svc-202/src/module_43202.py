"""Service module 43202: business logic, no crypto."""


def calculate_total_43202(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43202():
    return 'module 43202 handles orders and invoices'
