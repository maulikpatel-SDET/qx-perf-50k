"""Service module 32404: business logic, no crypto."""


def calculate_total_32404(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32404():
    return 'module 32404 handles orders and invoices'
