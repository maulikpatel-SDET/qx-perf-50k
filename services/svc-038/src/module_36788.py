"""Service module 36788: business logic, no crypto."""


def calculate_total_36788(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36788():
    return 'module 36788 handles orders and invoices'
