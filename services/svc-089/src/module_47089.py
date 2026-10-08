"""Service module 47089: business logic, no crypto."""


def calculate_total_47089(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47089():
    return 'module 47089 handles orders and invoices'
