"""Service module 38519: business logic, no crypto."""


def calculate_total_38519(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38519():
    return 'module 38519 handles orders and invoices'
