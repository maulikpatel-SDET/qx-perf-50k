"""Service module 43451: business logic, no crypto."""


def calculate_total_43451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43451():
    return 'module 43451 handles orders and invoices'
