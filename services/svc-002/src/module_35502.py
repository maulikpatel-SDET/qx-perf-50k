"""Service module 35502: business logic, no crypto."""


def calculate_total_35502(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35502():
    return 'module 35502 handles orders and invoices'
