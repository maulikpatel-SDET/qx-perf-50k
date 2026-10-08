"""Service module 18612: business logic, no crypto."""


def calculate_total_18612(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18612():
    return 'module 18612 handles orders and invoices'
