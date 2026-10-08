"""Service module 24703: business logic, no crypto."""


def calculate_total_24703(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24703():
    return 'module 24703 handles orders and invoices'
