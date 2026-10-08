"""Service module 6055: business logic, no crypto."""


def calculate_total_6055(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6055():
    return 'module 6055 handles orders and invoices'
