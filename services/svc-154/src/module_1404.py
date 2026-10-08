"""Service module 1404: business logic, no crypto."""


def calculate_total_1404(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1404():
    return 'module 1404 handles orders and invoices'
