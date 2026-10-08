"""Service module 48555: business logic, no crypto."""


def calculate_total_48555(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48555():
    return 'module 48555 handles orders and invoices'
