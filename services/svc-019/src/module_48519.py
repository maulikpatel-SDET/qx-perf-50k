"""Service module 48519: business logic, no crypto."""


def calculate_total_48519(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48519():
    return 'module 48519 handles orders and invoices'
