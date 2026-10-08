"""Service module 28089: business logic, no crypto."""


def calculate_total_28089(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28089():
    return 'module 28089 handles orders and invoices'
