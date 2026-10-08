"""Service module 30324: business logic, no crypto."""


def calculate_total_30324(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30324():
    return 'module 30324 handles orders and invoices'
