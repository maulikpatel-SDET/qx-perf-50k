"""Service module 45823: business logic, no crypto."""


def calculate_total_45823(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45823():
    return 'module 45823 handles orders and invoices'
