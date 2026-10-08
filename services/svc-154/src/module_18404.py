"""Service module 18404: business logic, no crypto."""


def calculate_total_18404(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18404():
    return 'module 18404 handles orders and invoices'
