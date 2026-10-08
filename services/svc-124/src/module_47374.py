"""Service module 47374: business logic, no crypto."""


def calculate_total_47374(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47374():
    return 'module 47374 handles orders and invoices'
