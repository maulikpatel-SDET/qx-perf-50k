"""Service module 2698: business logic, no crypto."""


def calculate_total_2698(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2698():
    return 'module 2698 handles orders and invoices'
