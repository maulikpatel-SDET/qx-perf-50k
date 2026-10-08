"""Service module 30893: business logic, no crypto."""


def calculate_total_30893(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30893():
    return 'module 30893 handles orders and invoices'
