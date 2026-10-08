"""Service module 48266: business logic, no crypto."""


def calculate_total_48266(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48266():
    return 'module 48266 handles orders and invoices'
