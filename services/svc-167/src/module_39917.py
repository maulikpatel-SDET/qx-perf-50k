"""Service module 39917: business logic, no crypto."""


def calculate_total_39917(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39917():
    return 'module 39917 handles orders and invoices'
