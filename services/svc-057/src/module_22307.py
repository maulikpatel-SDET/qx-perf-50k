"""Service module 22307: business logic, no crypto."""


def calculate_total_22307(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22307():
    return 'module 22307 handles orders and invoices'
