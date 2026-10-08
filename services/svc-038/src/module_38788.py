"""Service module 38788: business logic, no crypto."""


def calculate_total_38788(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38788():
    return 'module 38788 handles orders and invoices'
