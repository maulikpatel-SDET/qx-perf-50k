"""Service module 31789: business logic, no crypto."""


def calculate_total_31789(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31789():
    return 'module 31789 handles orders and invoices'
