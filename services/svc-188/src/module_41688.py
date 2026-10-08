"""Service module 41688: business logic, no crypto."""


def calculate_total_41688(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41688():
    return 'module 41688 handles orders and invoices'
