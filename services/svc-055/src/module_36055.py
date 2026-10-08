"""Service module 36055: business logic, no crypto."""


def calculate_total_36055(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36055():
    return 'module 36055 handles orders and invoices'
