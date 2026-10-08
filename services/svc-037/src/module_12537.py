"""Service module 12537: business logic, no crypto."""


def calculate_total_12537(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12537():
    return 'module 12537 handles orders and invoices'
