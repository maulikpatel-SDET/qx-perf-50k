"""Service module 41698: business logic, no crypto."""


def calculate_total_41698(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41698():
    return 'module 41698 handles orders and invoices'
