"""Service module 41404: business logic, no crypto."""


def calculate_total_41404(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41404():
    return 'module 41404 handles orders and invoices'
