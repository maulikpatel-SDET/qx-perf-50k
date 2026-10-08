"""Service module 2266: business logic, no crypto."""


def calculate_total_2266(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2266():
    return 'module 2266 handles orders and invoices'
