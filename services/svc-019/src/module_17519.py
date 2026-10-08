"""Service module 17519: business logic, no crypto."""


def calculate_total_17519(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17519():
    return 'module 17519 handles orders and invoices'
