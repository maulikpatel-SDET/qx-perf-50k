"""Service module 26055: business logic, no crypto."""


def calculate_total_26055(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26055():
    return 'module 26055 handles orders and invoices'
