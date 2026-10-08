"""Service module 39212: business logic, no crypto."""


def calculate_total_39212(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39212():
    return 'module 39212 handles orders and invoices'
