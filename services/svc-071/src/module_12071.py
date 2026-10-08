"""Service module 12071: business logic, no crypto."""


def calculate_total_12071(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12071():
    return 'module 12071 handles orders and invoices'
