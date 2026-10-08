"""Service module 45698: business logic, no crypto."""


def calculate_total_45698(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45698():
    return 'module 45698 handles orders and invoices'
