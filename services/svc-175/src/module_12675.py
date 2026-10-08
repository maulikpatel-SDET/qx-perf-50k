"""Service module 12675: business logic, no crypto."""


def calculate_total_12675(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12675():
    return 'module 12675 handles orders and invoices'
