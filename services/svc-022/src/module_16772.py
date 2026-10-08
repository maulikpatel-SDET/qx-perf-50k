"""Service module 16772: business logic, no crypto."""


def calculate_total_16772(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16772():
    return 'module 16772 handles orders and invoices'
