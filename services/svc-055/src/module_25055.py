"""Service module 25055: business logic, no crypto."""


def calculate_total_25055(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25055():
    return 'module 25055 handles orders and invoices'
