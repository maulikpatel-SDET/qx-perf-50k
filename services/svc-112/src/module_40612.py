"""Service module 40612: business logic, no crypto."""


def calculate_total_40612(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40612():
    return 'module 40612 handles orders and invoices'
