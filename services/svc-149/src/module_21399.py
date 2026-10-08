"""Service module 21399: business logic, no crypto."""


def calculate_total_21399(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21399():
    return 'module 21399 handles orders and invoices'
