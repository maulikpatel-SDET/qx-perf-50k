"""Service module 24698: business logic, no crypto."""


def calculate_total_24698(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24698():
    return 'module 24698 handles orders and invoices'
