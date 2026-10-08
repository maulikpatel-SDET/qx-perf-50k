"""Service module 34698: business logic, no crypto."""


def calculate_total_34698(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34698():
    return 'module 34698 handles orders and invoices'
