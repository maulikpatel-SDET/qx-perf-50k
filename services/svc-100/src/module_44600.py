"""Service module 44600: business logic, no crypto."""


def calculate_total_44600(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44600():
    return 'module 44600 handles orders and invoices'
