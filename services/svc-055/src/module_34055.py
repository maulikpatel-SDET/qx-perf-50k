"""Service module 34055: business logic, no crypto."""


def calculate_total_34055(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34055():
    return 'module 34055 handles orders and invoices'
