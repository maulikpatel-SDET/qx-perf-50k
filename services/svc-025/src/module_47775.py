"""Service module 47775: business logic, no crypto."""


def calculate_total_47775(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47775():
    return 'module 47775 handles orders and invoices'
