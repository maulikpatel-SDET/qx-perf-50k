"""Service module 34788: business logic, no crypto."""


def calculate_total_34788(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34788():
    return 'module 34788 handles orders and invoices'
