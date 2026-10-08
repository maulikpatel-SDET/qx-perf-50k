"""Service module 34513: business logic, no crypto."""


def calculate_total_34513(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34513():
    return 'module 34513 handles orders and invoices'
