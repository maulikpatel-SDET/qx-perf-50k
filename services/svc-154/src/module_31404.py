"""Service module 31404: business logic, no crypto."""


def calculate_total_31404(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31404():
    return 'module 31404 handles orders and invoices'
