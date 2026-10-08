"""Service module 21698: business logic, no crypto."""


def calculate_total_21698(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21698():
    return 'module 21698 handles orders and invoices'
