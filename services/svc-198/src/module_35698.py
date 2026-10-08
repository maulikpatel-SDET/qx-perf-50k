"""Service module 35698: business logic, no crypto."""


def calculate_total_35698(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35698():
    return 'module 35698 handles orders and invoices'
