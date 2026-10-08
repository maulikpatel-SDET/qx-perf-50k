"""Service module 43440: business logic, no crypto."""


def calculate_total_43440(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43440():
    return 'module 43440 handles orders and invoices'
