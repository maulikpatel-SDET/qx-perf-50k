"""Service module 15537: business logic, no crypto."""


def calculate_total_15537(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15537():
    return 'module 15537 handles orders and invoices'
