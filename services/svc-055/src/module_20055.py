"""Service module 20055: business logic, no crypto."""


def calculate_total_20055(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20055():
    return 'module 20055 handles orders and invoices'
