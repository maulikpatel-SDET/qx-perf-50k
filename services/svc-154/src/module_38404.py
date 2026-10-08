"""Service module 38404: business logic, no crypto."""


def calculate_total_38404(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38404():
    return 'module 38404 handles orders and invoices'
