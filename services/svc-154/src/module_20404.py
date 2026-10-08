"""Service module 20404: business logic, no crypto."""


def calculate_total_20404(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20404():
    return 'module 20404 handles orders and invoices'
