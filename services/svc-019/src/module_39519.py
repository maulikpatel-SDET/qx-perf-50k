"""Service module 39519: business logic, no crypto."""


def calculate_total_39519(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39519():
    return 'module 39519 handles orders and invoices'
