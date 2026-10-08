"""Service module 48579: business logic, no crypto."""


def calculate_total_48579(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48579():
    return 'module 48579 handles orders and invoices'
