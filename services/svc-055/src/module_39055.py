"""Service module 39055: business logic, no crypto."""


def calculate_total_39055(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39055():
    return 'module 39055 handles orders and invoices'
