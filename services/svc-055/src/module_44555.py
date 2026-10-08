"""Service module 44555: business logic, no crypto."""


def calculate_total_44555(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44555():
    return 'module 44555 handles orders and invoices'
