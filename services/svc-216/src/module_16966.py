"""Service module 16966: business logic, no crypto."""


def calculate_total_16966(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16966():
    return 'module 16966 handles orders and invoices'
