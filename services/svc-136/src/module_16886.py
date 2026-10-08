"""Service module 16886: business logic, no crypto."""


def calculate_total_16886(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16886():
    return 'module 16886 handles orders and invoices'
