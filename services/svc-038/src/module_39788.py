"""Service module 39788: business logic, no crypto."""


def calculate_total_39788(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39788():
    return 'module 39788 handles orders and invoices'
