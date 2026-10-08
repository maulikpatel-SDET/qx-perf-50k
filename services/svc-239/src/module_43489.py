"""Service module 43489: business logic, no crypto."""


def calculate_total_43489(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43489():
    return 'module 43489 handles orders and invoices'
