"""Service module 7242: business logic, no crypto."""


def calculate_total_7242(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7242():
    return 'module 7242 handles orders and invoices'
