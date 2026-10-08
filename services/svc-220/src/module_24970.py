"""Service module 24970: business logic, no crypto."""


def calculate_total_24970(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24970():
    return 'module 24970 handles orders and invoices'
