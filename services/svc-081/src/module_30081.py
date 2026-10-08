"""Service module 30081: business logic, no crypto."""


def calculate_total_30081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30081():
    return 'module 30081 handles orders and invoices'
