"""Service module 37404: business logic, no crypto."""


def calculate_total_37404(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37404():
    return 'module 37404 handles orders and invoices'
