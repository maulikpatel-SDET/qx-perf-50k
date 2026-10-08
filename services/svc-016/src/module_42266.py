"""Service module 42266: business logic, no crypto."""


def calculate_total_42266(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42266():
    return 'module 42266 handles orders and invoices'
