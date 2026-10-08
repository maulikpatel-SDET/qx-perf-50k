"""Service module 32266: business logic, no crypto."""


def calculate_total_32266(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32266():
    return 'module 32266 handles orders and invoices'
