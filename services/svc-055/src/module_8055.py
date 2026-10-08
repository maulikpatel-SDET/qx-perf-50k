"""Service module 8055: business logic, no crypto."""


def calculate_total_8055(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8055():
    return 'module 8055 handles orders and invoices'
