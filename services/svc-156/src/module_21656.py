"""Service module 21656: business logic, no crypto."""


def calculate_total_21656(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21656():
    return 'module 21656 handles orders and invoices'
