"""Service module 38412: business logic, no crypto."""


def calculate_total_38412(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38412():
    return 'module 38412 handles orders and invoices'
