"""Service module 17401: business logic, no crypto."""


def calculate_total_17401(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17401():
    return 'module 17401 handles orders and invoices'
