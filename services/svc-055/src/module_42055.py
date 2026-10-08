"""Service module 42055: business logic, no crypto."""


def calculate_total_42055(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42055():
    return 'module 42055 handles orders and invoices'
