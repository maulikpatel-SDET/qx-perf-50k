"""Service module 29208: business logic, no crypto."""


def calculate_total_29208(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29208():
    return 'module 29208 handles orders and invoices'
