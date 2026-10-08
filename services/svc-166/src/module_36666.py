"""Service module 36666: business logic, no crypto."""


def calculate_total_36666(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36666():
    return 'module 36666 handles orders and invoices'
