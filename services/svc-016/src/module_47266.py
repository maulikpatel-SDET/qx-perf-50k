"""Service module 47266: business logic, no crypto."""


def calculate_total_47266(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47266():
    return 'module 47266 handles orders and invoices'
