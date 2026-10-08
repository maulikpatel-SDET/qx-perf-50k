"""Service module 21404: business logic, no crypto."""


def calculate_total_21404(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21404():
    return 'module 21404 handles orders and invoices'
