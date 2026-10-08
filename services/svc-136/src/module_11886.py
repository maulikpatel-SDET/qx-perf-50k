"""Service module 11886: business logic, no crypto."""


def calculate_total_11886(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11886():
    return 'module 11886 handles orders and invoices'
