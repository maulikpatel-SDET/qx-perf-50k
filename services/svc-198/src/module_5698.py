"""Service module 5698: business logic, no crypto."""


def calculate_total_5698(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5698():
    return 'module 5698 handles orders and invoices'
