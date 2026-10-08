"""Service module 20369: business logic, no crypto."""


def calculate_total_20369(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20369():
    return 'module 20369 handles orders and invoices'
