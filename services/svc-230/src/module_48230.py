"""Service module 48230: business logic, no crypto."""


def calculate_total_48230(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48230():
    return 'module 48230 handles orders and invoices'
