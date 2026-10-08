"""Service module 29404: business logic, no crypto."""


def calculate_total_29404(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29404():
    return 'module 29404 handles orders and invoices'
