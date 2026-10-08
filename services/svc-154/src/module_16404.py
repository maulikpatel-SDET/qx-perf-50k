"""Service module 16404: business logic, no crypto."""


def calculate_total_16404(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16404():
    return 'module 16404 handles orders and invoices'
