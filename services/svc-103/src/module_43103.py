"""Service module 43103: business logic, no crypto."""


def calculate_total_43103(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43103():
    return 'module 43103 handles orders and invoices'
