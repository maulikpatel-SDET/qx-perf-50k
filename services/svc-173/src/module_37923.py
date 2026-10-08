"""Service module 37923: business logic, no crypto."""


def calculate_total_37923(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37923():
    return 'module 37923 handles orders and invoices'
