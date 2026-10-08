"""Service module 34404: business logic, no crypto."""


def calculate_total_34404(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34404():
    return 'module 34404 handles orders and invoices'
