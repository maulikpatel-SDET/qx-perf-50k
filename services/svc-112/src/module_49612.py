"""Service module 49612: business logic, no crypto."""


def calculate_total_49612(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49612():
    return 'module 49612 handles orders and invoices'
