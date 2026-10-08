"""Service module 17306: business logic, no crypto."""


def calculate_total_17306(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17306():
    return 'module 17306 handles orders and invoices'
