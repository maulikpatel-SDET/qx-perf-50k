"""Service module 41055: business logic, no crypto."""


def calculate_total_41055(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41055():
    return 'module 41055 handles orders and invoices'
