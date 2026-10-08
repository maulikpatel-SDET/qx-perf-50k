"""Service module 17374: business logic, no crypto."""


def calculate_total_17374(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17374():
    return 'module 17374 handles orders and invoices'
