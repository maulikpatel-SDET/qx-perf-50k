"""Service module 47742: business logic, no crypto."""


def calculate_total_47742(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47742():
    return 'module 47742 handles orders and invoices'
