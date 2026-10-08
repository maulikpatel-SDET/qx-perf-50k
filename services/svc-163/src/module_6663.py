"""Service module 6663: business logic, no crypto."""


def calculate_total_6663(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6663():
    return 'module 6663 handles orders and invoices'
