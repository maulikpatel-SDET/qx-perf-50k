"""Service module 7009: business logic, no crypto."""


def calculate_total_7009(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7009():
    return 'module 7009 handles orders and invoices'
